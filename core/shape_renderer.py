from typing import Optional, Tuple
from patterns import ShapePatterns


class ShapeRenderer:
    """Alakzat renderelésért felelős osztály."""
    
    def __init__(self, git_handler):
        self.git_handler = git_handler
        self.shape_patterns = ShapePatterns()
    
    def calculate_pattern_dimensions(self, pattern) -> Tuple[int, int]:
        """Kiszámítja egy minta szélességét és magasságát."""
        if not pattern or not pattern[0]:
            return 0, 0
        
        height = len(pattern)
        width = len(pattern[0]) if pattern else 0
        
        return width, height
    
    def draw_shape(self, shape_name: str, start_week: Optional[int] = None, start_day: Optional[int] = None, 
                   auto_center: bool = True, compact: bool = None):
        """
        Alakzatot rajzol a grid-re.
        
        Args:
            shape_name: Az alakzat neve (heart, star, smiley, diamond)
            start_week: Kezdő hét pozíció (None esetén automatikus középre igazítás)
            start_day: Kezdő nap pozíció (None esetén automatikus középre igazítás)
            auto_center: Automatikus középre igazítás engedélyezése
            compact: Nem használt paraméter (backward compatibility)
        """
        shapes = self.shape_patterns.get_patterns()
        
        if shape_name in shapes:
            shape_pattern = shapes[shape_name]
            
            # Automatikus középre igazítás
            if auto_center and (start_week is None or start_day is None):
                shape_width, shape_height = self.calculate_pattern_dimensions(shape_pattern)
                calc_week, calc_day = self._calculate_centered_position(shape_width, shape_height)
                
                start_week = start_week if start_week is not None else calc_week
                start_day = start_day if start_day is not None else calc_day
                
                print(f"📍 Automatikus pozicionálás: hét {start_week}, nap {start_day}")
                print(f"📏 Alakzat mérete: {shape_width}x{shape_height}")
            
            # Alapértelmezett értékek, ha nem lett megadva és nem is automatikus
            if start_week is None:
                start_week = 20
            if start_day is None:
                start_day = 0
            
            print(f"🎨 Alakzat rajzolása: {shape_name}")
            self.git_handler.draw_pattern(shape_pattern, start_week, start_day)
        else:
            print(f"❌ Ismeretlen alakzat: {shape_name}")
            print(f"📋 Elérhető alakzatok: {list(shapes.keys())}")
    
    def get_available_shapes(self, compact: bool = None) -> list:
        """Visszaadja az elérhető alakzatok listáját."""
        return list(self.shape_patterns.get_patterns().keys())
    
    def show_preview(self, pattern):
        """Megjeleníti egy minta előnézetét."""
        print("📋 Előnézet:")
        for row in pattern:
            line = ""
            for cell in row:
                line += "██" if cell == 1 else "  "
            print(f"   {line}")
    
    def _calculate_centered_position(self, content_width: int, content_height: int) -> Tuple[int, int]:
        """Kiszámítja a középre igazítás pozícióját."""
        # Középre igazítás X tengelyen (hetek)
        center_week = max(0, (self.git_handler.grid_width - content_width) // 2)
        
        # Középre igazítás Y tengelyen (napok)
        center_day = max(0, (self.git_handler.grid_height - content_height) // 2)
        
        return center_week, center_day 