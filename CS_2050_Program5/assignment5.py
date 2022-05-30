#!/usr/bin/python3
"""
Title: Assignment 5
Desc: To implement a function that uses a graph-search approach to produce a 
"path" that represents a solution to the water container problem.
"""
import math
import unittest

class findWaterContainerPath():
    """
    in this class we have functions to initialize the container variables,
    calculate the capacity of the containers and calculate the minumum state 
    """
    def variableState(self, capacity_a, capacity_b):
        """
        initialize variable state for container 
        """
        if capacity_b == 0:
            return capacity_a
        return variableState(capacity_b, capacity_a%capacity_b)

    def minimumState(self, x, y, z):
        """
        function to compare/calculate variable state against calc capacity
        if 
        """
        if y > x:
            temp = y
            y = x
            x = temp
        if (z%(variableState(x, y))!= 0):
            return -1
        return(min(CalculateCapacity(x, y, z), CalculateCapacity(y, x, z)))

    def CalculateCapacity(self, toCup, cups, toGlass, z):
        """
        function to calculate the capacity of cups, the distance to and from
        and reflected into the final capacity
        """
        fromCup = toCup
        toGlass = 0
        goal_amount = 1
        while ((fromCup != z) and (toGlass != z)):
            temp = min(fromCup, toCup-toGlass)
            toGlass = toGlass + temp
            fromCup = fromCup - temp
            goal_amount = goal_amount +1
            if ((fromCup == z) or (toGlass == z)):
                break
            if fromCup == 0:
                fromCup = cups
                goal_amount = goal_amount + 1
            if toGlass == toCup:
                toGlass = 0
                goal_amount = goal_amount +1
        return goal_amount
    """
    user input for cap a, cap b, and goal amount, printing out the lowest 
    number required to satisfy the function
    """
    capacity_a = int(input("Enter the capacity of container A: "))
    capacity_b = int(input("Enter the capacity of container B: "))
    goal_amount = int(input("Enter the goal quantity: "))
    print('Lowest number required for the goal amount:',minimumState(capacity_a, capacity_b, goal_amount))
    
    if int(goal_amount) % math.gcd(int(capacity_a), int(capacity_b)) == 0:
        path = findWaterContainerPath(int(capacity_a), int(capacity_b), int(goal_amount))
    else:
        print("No solution for containers with these sizes and with this final goal amount")
