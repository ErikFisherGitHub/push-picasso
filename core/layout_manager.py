from typing import List, Dict, Any, Tuple
import re


class LayoutManager:
    """Layout és elemek elhelyezését kezelő osztály."""
    
    def __init__(self, git_handler, text_renderer, shape_renderer):
        self.git_handler = git_handler
        self.text_renderer = text_renderer
        self.shape_renderer = shape_renderer
    
    def parse_text_with_shapes(self, text: str, compact: bool = None) -> List[Dict[str, Any]]:
        """
        Szöveget elemez és szétválasztja szöveg és alakzat elemekre.
        
        Args:
            text: Bemenet szöveg (pl. "Hello \"heart\" World")
            compact: Nem használt paraméter (backward compatibility)
            
        Returns:
            List[Dict]: Elemek listája
        """
        available_shapes = self.shape_renderer.get_available_shapes()
        
        elements = []
        current_pos = 0
        
        # Regex minta az alakzatok keresésére: "alakzat_név"
        shape_pattern = r'"(' + '|'.join(available_shapes) + r')"'
        
        for match in re.finditer(shape_pattern, text):
            # Szöveg hozzáadása az alakzat előtt (ha van)
            if match.start() > current_pos:
                text_before = text[current_pos:match.start()].strip()
                if text_before:
                    elements.append({
                        'type': 'text',
                        'content': text_before
                    })
            
            # Alakzat hozzáadása
            shape_name = match.group(1)
            elements.append({
                'type': 'shape',
                'content': shape_name
            })
            
            current_pos = match.end()
        
        # Szöveg hozzáadása az utolsó alakzat után (ha van)
        if current_pos < len(text):
            text_after = text[current_pos:].strip()
            if text_after:
                elements.append({
                    'type': 'text',
                    'content': text_after
                })
        
        # Ha nincs alakzat, az egész szöveg
        if not elements:
            elements.append({
                'type': 'text',
                'content': text.strip()
            })
        
        return elements
    
    def create_combined_art(self):
        """Kombinált art létrehozása szöveg és alakzatok keverékével."""
        print("🎨 Kombinált Art Létrehozása")
        print("=" * 50)
        
        # Szöveg bekérése
        text = input("📝 Mit írjunk ki? ").strip()
        
        if not text:
            print("❌ Üres szöveg!")
            return
        
        # Elemek feldolgozása
        elements = self.parse_text_with_shapes(text)
        
        print(f"\n🔍 Feldolgozott elemek:")
        for i, element in enumerate(elements):
            print(f"  {i+1}. {element['type']}: '{element['content']}'")
        
        # Layout elhelyezése
        self._place_inline_elements(elements)
        
        print("✅ Kombinált art sikeresen létrehozva!")
    
    def _place_inline_elements(self, elements: List[Dict[str, Any]]):
        """Elemeket egymás mellett helyezi el inline módban."""
        current_week = 0
        current_day = 1  # Középre igazítás Y tengelyen
        
        # Teljes szélesség kiszámítása az inline elhelyezéshez
        total_width = 0
        max_height = 0
        
        for element in elements:
            if element['type'] == 'text':
                width, height = self.text_renderer.calculate_text_dimensions(
                    element['content'], letter_spacing=1
                )
            else:  # shape
                shapes = self.shape_renderer.shape_patterns.get_patterns()
                pattern = shapes[element['content']]
                width, height = self.shape_renderer.calculate_pattern_dimensions(pattern)
            
            total_width += width + 1  # +1 az elemek közötti távolság
            max_height = max(max_height, height)
        
        # Kezdő pozíció középre igazítása
        start_week = max(0, (self.git_handler.grid_width - total_width) // 2)
        start_day = max(0, (self.git_handler.grid_height - max_height) // 2)
        
        print(f"📍 Teljes layout pozíció: hét {start_week}, nap {start_day}")
        print(f"📏 Teljes layout mérete: {total_width}x{max_height}")
        
        current_week = start_week
        
        # Elemek elhelyezése
        for element in elements:
            if element['type'] == 'text':
                print(f"📝 Szöveg elhelyezése: '{element['content']}'")
                self.text_renderer.write_text(
                    element['content'], 
                    start_week=current_week, 
                    start_day=start_day,
                    letter_spacing=1,
                    auto_center=False
                )
                width, _ = self.text_renderer.calculate_text_dimensions(
                    element['content'], letter_spacing=1
                )
                current_week += width + 1
            
            else:  # shape
                print(f"🎨 Alakzat elhelyezése: '{element['content']}'")
                self.shape_renderer.draw_shape(
                    element['content'],
                    start_week=current_week,
                    start_day=start_day,
                    auto_center=False
                )
                shapes = self.shape_renderer.shape_patterns.get_patterns()
                pattern = shapes[element['content']]
                width, _ = self.shape_renderer.calculate_pattern_dimensions(pattern)
                current_week += width + 1
    
    def _get_element_width(self, element: Dict[str, Any], compact: bool = None) -> int:
        """Visszaadja egy elem szélességét."""
        if element['type'] == 'text':
            width, _ = self.text_renderer.calculate_text_dimensions(
                element['content'], letter_spacing=1
            )
            return width
        else:  # shape
            shapes = self.shape_renderer.shape_patterns.get_patterns()
            pattern = shapes[element['content']]
            width, _ = self.shape_renderer.calculate_pattern_dimensions(pattern)
            return width
    
    def _place_elements_automatically(self, elements: List[Dict[str, Any]]):
        """Elemeket automatikusan helyezi el a legjobb elrendezésben."""
        # Egyszerű inline elhelyezés most
        self._place_inline_elements(elements)
    
    def _draw_layout_elements(self, elements: List[Dict[str, Any]]):
        """Kirajzolja az elemeket a megadott pozíciókban."""
        for element in elements:
            if element['type'] == 'text':
                self.text_renderer.write_text(
                    element['content'],
                    start_week=element.get('week', 0),
                    start_day=element.get('day', 0),
                    auto_center=False
                )
            else:  # shape
                self.shape_renderer.draw_shape(
                    element['content'],
                    start_week=element.get('week', 0),
                    start_day=element.get('day', 0),
                    auto_center=False
                ) 