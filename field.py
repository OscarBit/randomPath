
class Field:

    def __init__(self):
        self.coordinates_of_drunks = {}

    def add_drunk(self, drunk, coordinate):
        self.coordinates_of_drunks[drunk] = coordinate

    def move_drunk(self, drunk):
        delta_x, delta_y =  drunk.step()
        current_coordinate = self.coordinates_of_drunks[drunk]
        new_coordinate = current_coordinate.move(delta_x, delta_y)

        self.coordinates_of_drunks[drunk] = new_coordinate

    def drunk_position(self, drunk):
        return self.coordinates_of_drunks[drunk]

