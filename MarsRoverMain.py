#!/usr/bin/python3

# We import os to do basic interaction with command line
import os
# We import library that handles moves and rotations of a rover
from Rover import Rover

# initialise global variables
# amount of rovers that landed
rover_count = 2
# commands sent to rovers
instructions = {'L': 'tleft', 'R': 'tright', 'M': 'move'}

def main():
    data = []
    # initialise intersection rovers soon to be positions
    intersection = set([])
    results = []
    check_coords = []
    # count_a for rover_count for loop
    count_a = 1
    # count_b for instructions for loop
    count_b = 2
    # count_r for results loop
    count_r = 0
    
    # store file/command choice in variable 
    file = input('Are you using Command Line or File? Enter (C | command) or (F | file): ')
    # check to see if choice is correct
    if file in ['F', 'file']:
        # add file with instructions to input
        file = input('app < ')
        # check if file exists
        if os.path.exists(file):
            # get rover count 
            num_lines = sum(1 for line in open(file)) - 1
            # get rover count
            rover_count = int(num_lines / 2)
            # get values in to separate array and store into data
            f = open(file)
            lines  = [line.strip().split(':') for line in f.readlines()]
            data   = [pair[1] for pair in lines]    
            #get plateau points from input
            xmax, ymax = map(int, data[0].split())
            for _ in range(rover_count):
                x, y, bearing = data[count_a].split()
                count_a += 2
                # check to see that you havent deployed rovers with the same coordinates
                if [x, y, bearing] not in check_coords:
                    check_coords.append([x, y, bearing])
                    rover = Rover(int(x), int(y), xmax, ymax, bearing, intersection)
                    # iterate over instructions string
                    for i in data[count_b]:
                        if i not in 'MRL':
                            # exit if not valid instruction
                            print('invalid instruction "%s": use M or R or L - please try again' % i)
                        else:
                            # store and run instructions
                            getattr(rover, instructions[i])()
                    count_b += 2
                    intersection.add((rover.x, rover.y))
                    results.append((rover.x, rover.y, rover.bearing))
                else:
                    print('2 or more of your rovers share the same spot, please try again')
            for x, y, z in results:
                count_r = count_r + 1
                print('Rover%d:' % count_r, x, y, z)
        else:
            print('file does not exist, make sure file is in this directory')
    elif file in ['C', 'command']:
        rover_count = int(input('Deploy rovers count:'))
        # get plateau points from input
        xmax, ymax = map(int, input('Plateau:').split())
        # iterate over rover count
        for _ in range(rover_count):
            # get rover landings and NESW bearing
            x, y, bearing = input('Rover%d Landing:' % count_a).split()
            count_a += 1
            # check to see that you havent deployed rovers with the same landings
            if [x, y, bearing] not in check_coords:
                check_coords.append([x, y, bearing])
                rover = Rover(int(x), int(y), xmax, ymax, bearing, intersection)
                # iterate over instructions string
                for i in input('Rover%d Instructions:' % count_b):
                    if i not in 'MRL':
                        # exit if not valid instruction
                        print('Invalid instruction "%s": use M or R or L - please try again' % i)
                    else:
                        # store and run instructions
                        getattr(rover, instructions[i])()
                count_b += 1
                # add nrovers coords to intersection
                intersection.add((rover.x, rover.y))
                results.append((rover.x, rover.y, rover.bearing))
            else:
                print('2 or more of your rovers share the same spot, please try again')
        # print results
        print('------------\n OUTPUT\n------------')
        for x, y, z in results:
            count_r = count_r + 1
            print('Rover%d:' % count_r, x, y, z)
    else:
        print('Please enter the correct choice? Enter (C | command) or (F | file)')

if __name__ == '__main__':
    main()