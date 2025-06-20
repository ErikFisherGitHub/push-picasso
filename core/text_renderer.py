from typing import List, Optional, Tuple
from patterns import AlphabetPatterns


class TextRenderer:
    """Szöveg renderelésért felelős osztály."""
    
    def __init__(self, git_handler):
        self.git_handler = git_handler
        self.alphabet_patterns = AlphabetPatterns()
    
    def calculate_text_dimensions(self, text: str, letter_spacing: int = 1, compact: bool = None) -> Tuple[int, int]:
        """Kiszámítja egy szöveg teljes szélességét és magasságát."""
        if not text:
            return 0, 0
        
        alphabet = self.alphabet_patterns.get_patterns()
        total_width = 0
        height = 5  # Egységes 5 pixel magas
        
        for i, char in enumerate(text.upper()):
            if char in alphabet:
                letter_width = len(alphabet[char][0])  # 4 pixel széles
                total_width += letter_width
                
                # Betűköz hozzáadása (kivéve az utolsó betű után)
                if i < len(text) - 1:
                    total_width += letter_spacing
        
        return total_width, height
    
    def calculate_multiline_text_dimensions(self, lines: List[str], letter_spacing: int = 1, 
                                          line_spacing: int = 1, compact: bool = None) -> Tuple[int, int]:
        """Kiszámítja többsoros szöveg teljes dimenzióit."""
        if not lines:
            return 0, 0
        
        max_width = 0
        total_height = 0
        line_height = 5  # Egységes 5 pixel magas
        
        for i, line in enumerate(lines):
            line_width, _ = self.calculate_text_dimensions(line, letter_spacing)
            max_width = max(max_width, line_width)
            
            total_height += line_height
            if i < len(lines) - 1:  # Sorköz hozzáadása (kivéve az utolsó sor után)
                total_height += line_spacing
        
        return max_width, total_height
    
    def write_text(self, text: str, start_week: Optional[int] = None, start_day: Optional[int] = None, 
                   letter_spacing: int = 1, auto_center: bool = True, compact: bool = None):
        """
        Szöveget ír ki a grid-re.
        
        Args:
            text: A kiírandó szöveg
            start_week: Kezdő hét pozíció (None esetén automatikus középre igazítás)
            start_day: Kezdő nap pozíció (None esetén automatikus középre igazítás)
            letter_spacing: Betűk közötti távolság
            auto_center: Automatikus középre igazítás engedélyezése
            compact: Nem használt paraméter (backward compatibility)
        """
        alphabet = self.alphabet_patterns.get_patterns()
        
        # Automatikus középre igazítás
        if auto_center and (start_week is None or start_day is None):
            text_width, text_height = self.calculate_text_dimensions(text, letter_spacing)
            calc_week, calc_day = self._calculate_centered_position(text_width, text_height)
            
            start_week = start_week if start_week is not None else calc_week
            start_day = start_day if start_day is not None else calc_day
            
            print(f"📍 Automatikus pozicionálás: hét {start_week}, nap {start_day}")
            print(f"📏 Szöveg mérete: {text_width}x{text_height}")
        
        # Alapértelmezett értékek, ha nem lett megadva és nem is automatikus
        if start_week is None:
            start_week = 5
        if start_day is None:
            start_day = 0
            
        current_week = start_week
        
        print(f"📝 Szöveg kiírása: '{text}'")
        
        for char in text.upper():
            if char in alphabet:
                pattern = alphabet[char]
                self.git_handler.draw_pattern(pattern, current_week, start_day)
                current_week += len(pattern[0]) + letter_spacing
            else:
                print(f"⚠️  Ismeretlen karakter: {char}")
                current_week += 4  # Hely az ismeretlen karakternek (4 széles)
        
        print(f"✅ Szöveg kiírása befejezve!")
    
    def write_multiline_text(self, lines: List[str], start_week: Optional[int] = None, start_day: Optional[int] = None, 
                           letter_spacing: int = 1, line_spacing: int = 1, auto_center: bool = True, compact: bool = None):
        """
        Többsoros szöveget ír ki.
        
        Args:
            lines: A sorok listája
            start_week: Kezdő hét pozíció (None esetén automatikus középre igazítás)
            start_day: Kezdő nap pozíció (None esetén automatikus középre igazítás)
            letter_spacing: Betűk közötti távolság
            line_spacing: Sorok közötti távolság
            auto_center: Automatikus középre igazítás engedélyezése
            compact: Nem használt paraméter (backward compatibility)
        """
        # Automatikus középre igazítás
        if auto_center and (start_week is None or start_day is None):
            total_width, total_height = self.calculate_multiline_text_dimensions(lines, letter_spacing, line_spacing)
            calc_week, calc_day = self._calculate_centered_position(total_width, total_height)
            
            start_week = start_week if start_week is not None else calc_week
            start_day = start_day if start_day is not None else calc_day
            
            print(f"📍 Automatikus pozicionálás: hét {start_week}, nap {start_day}")
            print(f"📏 Többsoros szöveg mérete: {total_width}x{total_height}")
        
        # Alapértelmezett értékek, ha nem lett megadva és nem is automatikus
        if start_week is None:
            start_week = 5
        if start_day is None:
            start_day = 0
            
        current_day = start_day
        
        for i, line in enumerate(lines):
            print(f"📝 Sor {i+1}: '{line}'")
            # Kikapcsoljuk az automatikus központosítást az egyes soroknál, mert már mi kezeljük
            self.write_text(line, start_week, current_day, letter_spacing, auto_center=False)
            line_height = 5  # Egységes 5 pixel magas
            current_day += line_height + line_spacing
            
            if current_day + 5 > self.git_handler.grid_height:  # Ellenőrzés: van-e hely a következő sornak
                print("⚠️  Figyelem: A következő sor túlnyúlik a grid magasságán!")
                break
    
    def _calculate_centered_position(self, content_width: int, content_height: int) -> Tuple[int, int]:
        """Kiszámítja a középre igazítás pozícióját."""
        # Középre igazítás X tengelyen (hetek)
        center_week = max(0, (self.git_handler.grid_width - content_width) // 2)
        
        # Középre igazítás Y tengelyen (napok)
        center_day = max(0, (self.git_handler.grid_height - content_height) // 2)
        
        return center_week, center_day 