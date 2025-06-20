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
            
            # Art fájlok törlése a git index-ből is (ha vannak)
            try:
                # Ellenőrizzük van-e art_data mappa a git-ben
                result = subprocess.run(['git', 'ls-files', 'art_data/'], 
                                      capture_output=True, text=True, cwd=self.repo_path)
                if result.returncode == 0 and result.stdout.strip():
                    # Van art_data fájl a git-ben, távolítsuk el
                    subprocess.run(['git', 'rm', '-rf', 'art_data/'], cwd=self.repo_path)
                    subprocess.run(['git', 'commit', '-m', 'Törölve art adatok'], cwd=self.repo_path)
                    print("🔄 Art commit-ok eltávolítva a git history-ból")
            except Exception as git_error:
                print(f"⚠️  Git fájl törlés sikertelen: {git_error}")
            
            print("✅ Art adatok sikeresen törölve!")
            return True
        except Exception as e:
            print(f"❌ Hiba az art adatok törlésekor: {e}")
            return False 