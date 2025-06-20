from typing import Dict, List


class AlphabetPatterns:
    """Alfabetikus karakterek mintáit kezelő osztály."""
    
    def get_patterns(self, compact: bool = None) -> Dict[str, List[List[int]]]:
        """Egységes 5x4-es (5 magas, 4 széles) alfabetikus karakterek."""
        return {
            'A': [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1]
            ],
            'B': [
                [1, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 0]
            ],
            'C': [
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 1, 1, 1]
            ],
            'D': [
                [1, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 1, 0]
            ],
            'E': [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 1, 1]
            ],
            'F': [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0]
            ],
            'G': [
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 1, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 1]
            ],
            'H': [
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1]
            ],
            'I': [
                [1, 1, 1, 1],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [1, 1, 1, 1]
            ],
            'J': [
                [0, 0, 0, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0]
            ],
            'K': [
                [1, 0, 0, 1],
                [1, 0, 1, 0],
                [1, 1, 0, 0],
                [1, 0, 1, 0],
                [1, 0, 0, 1]
            ],
            'L': [
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 1, 1, 1]
            ],
            'M': [
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1]
            ],
            'N': [
                [1, 0, 0, 1],
                [1, 1, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 1, 1],
                [1, 0, 0, 1]
            ],
            'O': [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0]
            ],
            'P': [
                [1, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0]
            ],
            'Q': [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 0, 1, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 1]
            ],
            'R': [
                [1, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 0, 0, 1]
            ],
            'S': [
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 1, 0]
            ],
            'T': [
                [1, 1, 1, 1],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0]
            ],
            'U': [
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0]
            ],
            'V': [
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0],
                [0, 1, 1, 0]
            ],
            'W': [
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 1]
            ],
            'X': [
                [1, 0, 0, 1],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [1, 0, 0, 1]
            ],
            'Y': [
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0]
            ],
            'Z': [
                [1, 1, 1, 1],
                [0, 0, 0, 1],
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 1, 1]
            ],
            ' ': [
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0]
            ]
        } 