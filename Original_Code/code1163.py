from itertools import product


class GameOfLife():
    def __init__(self, width, height, strs):
        """""" (int, int, str) => obj
        GOL constructor.""""""
        self.width = width
        self.height = height
        self.field = strs
        self.fillCell = ""X""
        self.emptyCell = "".""

    def __createField(self):
        """""" Creates empty field for the game obj.""""""
        self.field = [[0]*self.width for _ in range(self.height)]
        
    @staticmethod
    def getMovesToNeighbours():
        """""" () => iterator((int, int))
        Returns iterator which gives all possible
        movements from any cell to it's
        neighbours.""""""
        directions = (-1, 0, 1)
        return filter(lambda x: x[0] or x[1],
                      product(directions, directions))

    def getNewCoords(self, cell, move):
        """"""((int, int), (int, int)) => (int, int)
        Compute new coords in the field of the game,
        by summ coordinates of the given cell and
        values of move. If new coordinates are lied
        outside the field, correct them.""""""
        row = (cell[0] + move[0]) % self.height
        col = (cell[1] + move[1]) % self.width
        return (row, col)
        
    def getNeighbours(self, cell):
        """""" (tuple(int,int,...)) => iterator(iterator(int))
        By given coordinates of cell, gets iterator by
        neighbours cells, which returns iterators by
        coordinates of a neighbour cell.""""""
        return map(lambda move: self.getNewCoords(cell, move),
                   GameOfLife.getMovesToNeighbours())

    def isLiveCell(self, cell):
        """""" ((row, col) => bool
        Returns true, if cell contains life. Otherwise it returns
        false. Cell is a tuple of coordinates (row, col).""""""
        return self.field[cell[0]][cell[1]] == self.fillCell

    def willLive(self, state, nbs):
        """"""(char, int) => char
        Define will cell of given state be alive
        on the next step, if it has ngs neighbours.""""""
        if state == self.emptyCell:
            return self.fillCell if nbs == 3 else self.emptyCell
        return self.fillCell if nbs in [2,3] else self.emptyCell
        
    def countNeighbours(self, cell):
        """""" ((int, int)) => int
        Count number of neighbours alive in the field.
        Cell is a tuple of coordinates (row, col).""""""
        return sum(map(lambda x: gol.isLiveCell(x),
                       self.getNeighbours((cell))))
            
    def countAllNeighbours(self):
        """""" () => [[int]]
        Return array with counts of neighbours for
        every cell on the field of the game.""""""
        res = [[self.countNeighbours((h, w))
                for w in range(self.width)]
               for h in range(self.height)]
        return res
    
    def getNextState(self):
        """"""() => [str]
        Return new field next to the current.""""""
        nbCnt = self.countAllNeighbours()
        res = ["""".join([self.willLive(state, nbs) for state, nbs in zline])
               for zline in map(zip, self.field, nbCnt)]
        return res

    @staticmethod
    def fieldToStr(field):
        return ""\n"".join(field)


h,w = map(int, input().split(' '))
strs = [input() for _ in range(h)]
gol = GameOfLife(w, h, strs)
next = gol.getNextState()
print(GameOfLife.fieldToStr(next))
 