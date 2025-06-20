import os
import stat
import shutil
import subprocess
import datetime
from typing import Tuple, Optional


class GitHandler:
    """Git repository műveletek kezelése."""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
        self.start_date = datetime.date(2024, 6, 16)  # Vasárnap
        self.grid_width = 53  # Hetek száma
        self.grid_height = 7  # Napok száma (0=vasárnap, 6=szombat)
    
    def date_to_grid_pos(self, date: datetime.date) -> Tuple[int, int]:
        """Dátumot grid pozícióvá konvertál."""
        delta = date - self.start_date
        week = delta.days // 7
        day = delta.days % 7
        return week, day
    
    def grid_pos_to_date(self, week: int, day: int) -> datetime.date:
        """Grid pozíciót dátummá konvertál."""
        delta = datetime.timedelta(days=week * 7 + day)
        return self.start_date + delta
    
    def create_commit(self, date: datetime.date, commits_count: int = 1):
        """Létrehoz commit-okat a megadott dátumra."""
        for i in range(commits_count):
            # Fájl név generálása dátum és sorszám alapján
            filename = f"art_data/{date.strftime('%Y-%m-%d')}_{i+1}.txt"
            
            # Könyvtár létrehozása, ha nem létezik
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            # Fájl tartalom
            content = f"Art data for {date} - entry {i+1}"
            
            # Fájl írása
            with open(filename, 'w') as f:
                f.write(content)
            
            # Git add
            subprocess.run(['git', 'add', filename], cwd=self.repo_path)
            
            # Commit készítése a megadott dátummal
            env = os.environ.copy()
            commit_datetime = datetime.datetime.combine(date, datetime.time(12, 0, 0))
            env['GIT_AUTHOR_DATE'] = commit_datetime.isoformat()
            env['GIT_COMMITTER_DATE'] = commit_datetime.isoformat()
            
            commit_message = f"Art commit for {date}"
            subprocess.run(['git', 'commit', '-m', commit_message], 
                         cwd=self.repo_path, env=env)
    
    def draw_pattern(self, pattern, start_week: int = 0, start_day: int = 0):
        """Rajzol egy mintát a grid-re."""
        for row_idx, row in enumerate(pattern):
            for col_idx, cell in enumerate(row):
                if cell == 1:  # Csak az 1-es értékekre rajzolunk
                    week = start_week + col_idx
                    day = start_day + row_idx
                    
                    # Ellenőrizzük, hogy a pozíció a grid-en belül van-e
                    if 0 <= week < self.grid_width and 0 <= day < self.grid_height:
                        date = self.grid_pos_to_date(week, day)
                        self.create_commit(date, commits_count=1)
    
    def init_git_repo(self):
        """Inicializálja a Git repository-t."""
        if not os.path.exists(os.path.join(self.repo_path, '.git')):
            subprocess.run(['git', 'init'], cwd=self.repo_path)
            print("ℹ️  Git repository létrehozva.")
        else:
            print("ℹ️  Git repository már létezik.")
    
    def get_repository_stats(self):
        """Visszaadja a repository statisztikáit."""
        try:
            result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], 
                                  capture_output=True, text=True, cwd=self.repo_path)
            total_commits = int(result.stdout.strip()) if result.returncode == 0 else 0
            
            result = subprocess.run(['git', 'log', '--oneline'], 
                                  capture_output=True, text=True, cwd=self.repo_path)
            commits_today = len([line for line in result.stdout.split('\n') 
                               if datetime.date.today().strftime('%Y-%m-%d') in line])
            
            return total_commits, commits_today
        except:
            return 0, 0
    
    def _remove_readonly_dir(self, directory_path: str):
        """Csak olvasható könyvtárak törlésének segédfüggvénye."""
        def handle_readonly_files(func, path, exc_info):
            if os.path.exists(path):
                os.chmod(path, stat.S_IWRITE)
                func(path)
        
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path, onerror=handle_readonly_files)
    
    def clean_repository(self):
        """Helyi art adatok tisztítása (git repository megtartva)."""
        try:
            # Csak az art_data mappa törlése, .git mappa megmarad
            art_data_dir = os.path.join(self.repo_path, 'art_data')
            self._remove_readonly_dir(art_data_dir)
            
            # Git history reset a kezdeti commit-ra (ha van)
            try:
                # Megnézzük, van-e initial commit
                result = subprocess.run(['git', 'log', '--oneline'], 
                                      capture_output=True, text=True, cwd=self.repo_path)
                if result.returncode == 0 and result.stdout.strip():
                    # Van commit history, reseteljük a legelsőre
                    first_commit = subprocess.run(['git', 'rev-list', '--max-parents=0', 'HEAD'], 
                                                capture_output=True, text=True, cwd=self.repo_path)
                    if first_commit.returncode == 0 and first_commit.stdout.strip():
                        first_commit_hash = first_commit.stdout.strip()
                        subprocess.run(['git', 'reset', '--hard', first_commit_hash], cwd=self.repo_path)
                        print("🔄 Git history visszaállítva az első commit-ra")
            except Exception as git_error:
                print(f"⚠️  Git history reset sikertelen: {git_error}")
            
            print("✅ Art adatok sikeresen törölve!")
            return True
        except Exception as e:
            print(f"❌ Hiba az art adatok törlésekor: {e}")
            return False
    
    def clean_github_repository(self):
        """GitHub repository teljes tisztítása."""
        try:
            # Próbáljuk meg lekérni a távoli URL-t
            remote_url = self.get_remote_url()
            if not remote_url:
                print("❌ Nincs beállított távoli repository!")
                return False
            
            current_branch = self.get_current_branch()
            if not current_branch:
                print("❌ Nem sikerült meghatározni a jelenlegi branch-et!")
                return False
            
            print(f"🔄 GitHub repository tisztítása...")
            print(f"📍 Repository: {remote_url}")
            print(f"🌿 Branch: {current_branch}")
            
            # Lokális tisztítás először
            if not self.clean_repository():
                return False
            
            # Git repo újrainicializálása
            self.init_git_repo()
            
            # README.md létrehozása (hogy legyen mit commit-olni)
            readme_content = """# GitHub Art Generator

Ez a repository a GitHub Art Generator által generált commit történetet tartalmazza.
"""
            with open(os.path.join(self.repo_path, 'README.md'), 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            # Első commit
            subprocess.run(['git', 'add', 'README.md'], cwd=self.repo_path)
            subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=self.repo_path)
            
            # Remote hozzáadása
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=self.repo_path)
            
            # Force push az új történettel
            result = subprocess.run(['git', 'push', '-f', 'origin', current_branch], 
                                  cwd=self.repo_path, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ GitHub repository sikeresen megtisztítva!")
                print("🎉 Az új, tiszta repository elérhető a GitHub-on!")
                return True
            else:
                print(f"❌ Hiba a GitHub push során: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Hiba a GitHub repository tisztítása során: {e}")
            return False
    
    def get_remote_url(self):
        """Visszaadja a remote repository URL-t."""
        try:
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                  capture_output=True, text=True, cwd=self.repo_path)
            return result.stdout.strip() if result.returncode == 0 else None
        except:
            return None
    
    def get_current_branch(self):
        """Visszaadja a jelenlegi branch nevét."""
        try:
            result = subprocess.run(['git', 'branch', '--show-current'], 
                                  capture_output=True, text=True, cwd=self.repo_path)
            return result.stdout.strip() if result.returncode == 0 else None
        except:
            return None 