from typing import Dict, List


class ShapePatterns:
    """Alakzat mintákat kezelő osztály."""
    
    def get_patterns(self, compact: bool = None) -> Dict[str, List[List[int]]]:
        """Egységes 5x5-ös alakzat minták."""
        return {
            'heart': [
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0]
            ],
            'star': [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [1, 0, 1, 0, 1]
            ],
            'smiley': [
                [0, 1, 1, 1, 0],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0]
            ],
            'diamond': [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0]
            ]
        } 