class Rook(ChessPiece):
    """class Rook that subclasses ChessPiece.

    """
    prefix = 'R'
    def __init__(self,position):
        """ rock constructor
        args:
        the algebraic notation of the new position to be moved.
        """
        ChessPiece.is_legal_move(self, position)
        self.position = position
        
        

    
    def is_legal_move(self, position):
       
        if ChessPiece.is_legal_move(self, position):
           
            if self.position[0] is position[0] or self.position[1] is position[1]:
                print self.position, position
                return True  
            else:
                print self.position, position
                return False
 """ Rook constructor
        args:
        the algebraic notation of the new position to be moved.
        """
        """ a fuction that test if the Bishop suggested move is a legal move

        args:
            postion(string): the  algebraic notation of the new position to
                             which this piece should be moved
            return (bool):
                Return True if the move is legal and False if it is not
        example:
        >>> rook = Rook('a1')
        >>> rook.prefix
        'R'
        >>> rook.move('b2')
        False
        >>> rook.move('h1')
        ('Ra1', 'Rh1', 1413252817.89340)
        >>> rook.move('h8')
        ('Rh1', 'Rh8', 1413252818.89340)
        
        """
