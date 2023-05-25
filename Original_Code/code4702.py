# put your python code here
class Box:
    def __init__(self, dimensions):
        self.length, self.width, self.height = dimensions

    def __eq__(self, other):
        if isinstance(other, Box):
            return self.length == other.length and self.width == other.width and self.height == other.height
        return False

    def __le__(self, other):
        if isinstance(other, Box):
            return self.length <= other.length and self.width <= other.width and self.height <= other.height
        return False

    def __ge__(self, other):
        if isinstance(other, Box):
            return self.length >= other.length and self.width >= other.width and self.height >= other.height
        return False


box1, box2 = Box(sorted(int(input()) for _ in range(3))), Box(sorted(int(input()) for _ in range(3)))
if box1 == box2:
    print('Boxes are equal')
elif box1 <= box2:
    print('The first box is smaller than the second one')
elif box1 >= box2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable') 