from drunk import RegularDrunk
from field import Field
from coordinate import Coordinate

def walk(field, drunk_man, steps):
    begining = field.drunk_position(drunk_man)

    for _ in range(steps):
        field.move_drunk(drunk_man)

    return begining.distance(field.drunk_position(drunk_man))

def walk_simulation(steps, numbers_of_trys, type_of_drunk):
    drunk_man = type_of_drunk(name='Oscarin')
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(numbers_of_trys):
        field = Field()
        field.add_drunk(drunk_man, origin)
        walk_simulation = walk(field, drunk_man, steps)
        distances.append(round(walk_simulation,1))

    return distances

def main(steps_of_the_walk, numbers_of_trys, type_of_drunk):

    for steps in steps_of_the_walk:
        distances = walk_simulation(steps, numbers_of_trys, type_of_drunk)
        average_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        print(f'{type_of_drunk.__name__} random path of {steps} steps')
        print(f'Average distance: {average_distance}')
        print(f'MAX: {max_distance}')
        print(f'MIN: {min_distance}\n')

if __name__ == '__main__':
    steps_of_the_walk = [10, 100, 1_000, 10_000]
    numbers_of_trys = 100

    main(steps_of_the_walk, numbers_of_trys, RegularDrunk)

