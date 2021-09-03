
# initialise global variables
# orientation list
orient = ['N', 'E', 'S', 'W']
# movement of rovers, 1 plateau point
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

class Rover:
    """
    calculate and return position of rovers based on input paramters
    """

    def __init__(self, x, y, xmax, ymax, bearing, intersection):
        """
        initialise parameters
        """
        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.bearing = bearing
        self.intersection = set(intersection)

    def tright(self):
        """
        turning right method
        """
        self.bearing = orient[(orient.index(self.bearing) + 1) % len(orient)]

    def tleft(self):
        """
        turning left method
        """
        self.bearing = orient[(orient.index(self.bearing) - 1) % len(orient)]

    def move(self):
        """
        moving forward 1 grid point method
        """
        xmod = self.x + move[self.bearing][0]
        ymod = self.y + move[self.bearing][1]
        # check intersection to see if nrover is not the same position as mrover
        if (xmod, ymod) not in self.intersection:
            if xmod <= self.xmax and xmod >= 0:
                self.x = xmod
            if ymod <= self.ymax and ymod >= 0:
                self.y = ymod
            else:
                print('Out of bounds, please try again!!')
        else:
            print('rovers cannot occupy the same spot, try again!!')