#!/usr/bin/env python3
"""
Push Picasso - Fő alkalmazás
Objektumorientált, moduláris felépítés
Egységes méretkonvenció: Szövegek 5x4, Alakzatok 5x5
"""

import signal
import sys
from core import GitHandler, TextRenderer, ShapeRenderer, LayoutManager


class PushPicasso:
    """Fő alkalmazás osztály."""
    
    def __init__(self, repo_path: str = "."):
        # Core komponensek inicializálása
        self.git_handler = GitHandler(repo_path)
        self.text_renderer = TextRenderer(self.git_handler)
        self.shape_renderer = ShapeRenderer(self.git_handler)
        self.layout_manager = LayoutManager(self.git_handler, self.text_renderer, self.shape_renderer)
        
        # Grid információk
        self.grid_width = self.git_handler.grid_width
        self.grid_height = self.git_handler.grid_height
        self.start_date = self.git_handler.start_date
        self.end_date = self.git_handler.grid_pos_to_date(self.grid_width - 1, self.grid_height - 1)
    
    def safe_input(self, prompt: str, timeout: int = 30) -> str:
        """Biztonságos input bekérés timeout-tal."""
        try:
            return input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Kilépés...")
            sys.exit(0)
    
    def show_main_menu(self):
        """Főmenü megjelenítése."""
        print("\n" + "─" * 54)
        print("🎯 Push Picasso - Főmenü")
        print("─" * 54)
        print("1. 🎨 Art létrehozása (szöveg + alakzatok)")
        print("2. 👀 Elérhető alakzatok listája")
        print("3. 🗑️  Art adatok törlése (commit history reset)")
        print("4. 🚪 Kilépés")
    
    def show_available_shapes(self):
        """Elérhető alakzatok megjelenítése."""
        print("\n🎨 Elérhető alakzatok (5x5-ös méret):")
        print("=" * 40)
        
        # Alakzatok listája
        shapes = self.shape_renderer.shape_patterns.get_patterns()
        
        for shape_name, pattern in shapes.items():
            print(f"\n🔹 {shape_name}:")
            self.shape_renderer.show_preview(pattern)
        
        print(f"\n💡 Használat: Írj be '\"alakzat_név\"' a szövegbe")
        print(f"   Például: 'Hello \"heart\" World'")
        print(f"\n📏 Méretkonvenció:")
        print(f"   • Szövegek: 5 magas × 4 széles")
        print(f"   • Alakzatok: 5 magas × 5 széles")
    
    def run(self):
        """Fő alkalmazás futtatása."""
        # Git repo inicializálása
        self.git_handler.init_git_repo()
        
        # Kezdő információk
        print("🎨 Push Picasso")
        print("=" * 60)
        
        while True:
            try:
                self.show_main_menu()
                choice = self.safe_input("\nVálassz egy opciót (1-4): ").strip()
                
                if choice == '1':
                    self.layout_manager.create_combined_art()
                elif choice == '2':
                    self.show_available_shapes()
                elif choice == '3':
                    self.git_handler.clean_repository()
                elif choice == '4':
                    print("👋 Viszlát!")
                    break
                else:
                    print("❌ Érvénytelen választás!")
                    
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Viszlát!")
                break


def signal_handler(sig, frame):
    """Signal handler a tiszta kilépéshez."""
    print('\n\n👋 Viszlát!')
    sys.exit(0)


def main():
    """Fő függvény."""
    # Signal handler beállítása
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Alkalmazás indítása
        app = PushPicasso()
        app.run()
        
        print("\n✅ Program befejezve!")
        print("💡 Ne felejtsd el a változtatásokat feltölteni GitHub-ra:")
        print("   git remote add origin <repository-url>")
        print("   git push -u origin <branch-név>")
        print("💡 A jelenlegi branch nevét a 'git branch' paranccsal tudod megnézni.")
        
    except Exception as e:
        print(f"❌ Váratlan hiba: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 