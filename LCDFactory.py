

_H_LINE = '-'
_V_LINE = '|'
_SPACE = ' '

# Horizontal mapping of the lines
_HORIZONTAL_MAP ={'1': (0, 0, 0),
                  '4': (0, 1, 0),
                  '7': (1, 0, 0),
                  '0': (1, 0, 1),
                  '*': (1, 1, 1)}

# Vertical mapping of the lines.
_VERTICAL_MAP =  {'1': (0, 1, 0, 1),
                  '2': (0, 1, 1, 0),
                  '3': (0, 1, 0, 1),
                  '4': (1, 1, 0, 1),
                  '5': (1, 0, 0, 1),
                  '6': (1, 0, 1, 1),
                  '7': (0, 1, 0, 1),
                  '8': (1, 1, 1, 1),
                  '9': (1, 1, 0, 1),
                  '0': (1, 1, 1, 1)}

class LCDFactory:

    def __init__(self, spacing=1):
        self.spacing = spacing        


    def printSequence(self, sequence, size):
        """Method for printing a given sequence in some size.

        Keyword arguments:
        sequence -- the string with the sequence
        size -- the integer with the size of the sequence
        """

        sequence_matrix = [self._factorRepresentation(character, size) for character in sequence]

        # Print the sequence
        for row in range(2*size+3):
            line = ''
            for character_matrix in sequence_matrix:
                line += ''.join(character_matrix[row][:])
                line += _SPACE*self.spacing
            print(line)

    def _factorRepresentation(self, character, size):
        """Matrix representation of a given character in some size"""
        # Create the character matrix space
        rows = 2*size + 3
        cols = size + 2
        char_matrix = [[_SPACE]*cols for i in range(rows)] 

        # Creates the constituent element
        horizontal_line = [_H_LINE]*size
        vertical_line = [_V_LINE]*size

        # Get the points to construct the number with the elements
        horizontal_points = self._getHLinesPoints(character, size)
        vertical_points = self._getVLinesPoints(character, size)

        for x, y in horizontal_points:
            char_matrix[x][y:y+size] = horizontal_line

        for x, y in vertical_points:
            for i in range(size):
                char_matrix[x+i][y] = vertical_line[i]

        return char_matrix

    def _getHLinesPoints(self, character, size):
        """(x, y) Positions of Horizontal lines, return a list"""
        if character in _HORIZONTAL_MAP.keys():
            hline_map = _HORIZONTAL_MAP[character] #(3 dimension tuple)
        else:
            hline_map = _HORIZONTAL_MAP['*']
        
        # i*(size+1) fit the position series in the rows
        hline_points = [(i*(size+1) ,1) for i in range(3) if hline_map[i] == 1]
        return hline_points

    def _getVLinesPoints(self, character, size):
        """(x, y) Positions of vertical lines, return a list"""
        vline_map = _VERTICAL_MAP[character]
        vline_positions = [(1, 0), (1, size+1), (size+2, 0), (size+2, size+1)]
        
        vline_points = [vline_positions[i] for i in range(4) if vline_map[i] == 1]
        return vline_points

