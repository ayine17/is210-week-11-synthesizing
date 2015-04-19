#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 11 syn module"""


import time


class ChessPiece(object):
    """ object of chessPiece class

    attribute:
        prefix (string): by default, set as an empty string
    """

    prefix = ''

    def __init__(ChessPiece, position):
        """ chessPiece construct
        args:
            position (string):
                stores the tile notation of its current position (eg, 'a8')
            moves Lists):
                list that stores tuples of information about each move
         attributes:
            position (string):
                stores the tile notation of its current position (eg, 'a8')
            moves Lists):
                list that stores tuples of information about each move

            return:
                move(lists):
                    lists of the postion of each move
            example
                >>> piece = ChessPiece('a1')
                >>> piece.position
                'a1'
        """
        
        if ChessPiece.is_legal_move(position):
            ChessPiece.position = position

            ChessPiece.moves = []
        else:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """class function that takes a single string argument, tile, and convert
           it to a tuple with two values, a 0-based y-coordinate and a 0-based
           x-coordinate

        args:
            tile(string): string to be converts it to a tuple with two values,
                          a 0-based y-coordinate and a 0-based x-coordinate.
        attributes:
            tile(string): string to be converts it to a tuple with two values,
                          a 0-based y-coordinate and a 0-based x-coordinate.
        return:
            tuples of valid move or none if not invalid
        example:
            >>> piece.algebraic_to_numeric('e7')
            (4,6)
            >>> piece.algebraic_to_numeric('j9')
            None
            >>> piece.move('j9')
            False
        """

        newtile = []
        algebraicnotation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        numericnotation = range(1, 9)

        for numeric in numericnotation:
            for algebraic in algebraicnotation:
                newtile.append(algebraic + str(numeric))
        if tile in newtile:
            x_cord = algebraicnotation.index(tile[0])
            y_cord = numericnotation.index(int(tile[1]))
            return x_cord, y_cord
        else:
            return None

    def is_legal_move(self, position):
        """ a fuction that test if the suggested move is a legal move

        args:
            postion(string): the  algebraic notation of the new position to
                             which this piece should be moved
            return (bool):
                Return True if the move is legal and False if it is not
            example:
            piece = ChessPiece('e91')
            Traceback (most recent call last):
            File "<pyshell#216>", line 1, in <module>
            piece = ChessPiece('e91')
            raise ValueError(excep.format(position))
            ValueError: `e91` is not a legal start position
            example:
            >>> piece = ChessPiece('e1')
            >>> piece.move('e7')
            [('e1', 'e7', 1429395759.478843)]

        """

        if self.algebraic_to_numeric(position) is None:

            return False
        else:
            return True

    def move(self, position):
        """a function to actually move our piece.

        args:
            the algebraic notation of the new position to be moved.
        return:
            Return the above tuple is position is a valid move or
            If it is not legal, return False
        """
        moves = ()
        if self.is_legal_move(position):
            oldposition = self.prefix + self.position
            newposition = self.prefix + position
            moves = ((oldposition, newposition, time.time()))
            self.moves.append(moves)
            
           # self.position = newposition
           # position = self.prefix + position
            return moves
        else:
            return False


class Rook(ChessPiece):
    """class Rook that subclasses ChessPiece.

    """
    prefix = 'R'
    def __init__(self,position):
        """ rock constructor
        args:
        the algebraic notation of the new position to be moved.
        """
        
        self.position = position
        
        

    
    def is_legal_move(self, position):
        self .positon = position
        if ChessPiece.is_legal_move(self, position):
           
            if self.position[0] == position[0] or self.position[1] == position[1]:
                print self.position, position
                return True  
            else:
                print self.position, position
                return False
