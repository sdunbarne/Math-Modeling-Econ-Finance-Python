#! /usr/bin/env python

from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # all walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            #Decide which direction to go and how far to go in that direction
            x_direction = choice([-1,1])
            x_distance  = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance  = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
## NAME: random_walk.py
## USAGE:  from random_walk import RandonWalk
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: A Python class to implenent a simulation of a random walk
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: Python3
## DEPENDENCIES: The choice function from the random package
## INCOMPATIBILITIES: none known
## PROVENANCE: Copied from pages 332-333 of Python Crash Course, by Eric Matthes
##             No Starch Press, 2016
## BUGS AND LIMITATIONS:  non eknown
## FEATURES AND POTENTIAL IMPROVEMENTS:  From a mathematical point of view
##            the step length Unif([0,1,2,3,4]) is non-standard, but this
##            could be easily changed and or modified.  This is also a two
##            dimensional random walk on the integer lattice, the
##            two-dimensional aspect again being mathematically a degree
#             more than necessary.
## AUTHOR:  Steve Dunbar
## VERSION:  1.0 as of Wed Oct  5, 2016  7:44 PM
## KEYWORDS: Python Class

