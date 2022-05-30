#!/usr/bin/python3
"""
Title: Assignment 4
Desc: The purpose of this program is to implement functions to 
build, evaluate, and print expressions using our (made-up) maybe-probably logic
"""
import operator
import random
import unittest

from binarytree import BinaryTree

from stack import Stack

"""
calculate function generating random number
"""
def calculate(p):
    return random.random() <= p
    
"""
this function takes a string as input and should return 
the binary tree representing the parse tree 
"""
def buildMPLogicParseTree(s):
    slist = s.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in slist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['T', 'F']:
            if i == 'T':
                i = True
            else:
                i = False
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent

        elif i == 'AND' or i == 'OR':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif any(x in i for x in ['P_', 'M_']):
            mp, fac = i.split('_')
            fac = float(fac)

            """
            Check to make sure is within range
            """
            if mp == 'M' and not (0.0 <= fac <= 0.75):
                print('If maybe is defined, the probability must be <= 0.75')
                return None

            if mp == 'P' and not (0.75 <= fac <= 1.0):
                print('If probably is defined, the probability must be >= 0.75')
                return None

            currentTree.setRootVal(fac)
            parent = pStack.pop()
            currentTree = parent

        elif i == ')':
            currentTree = pStack.pop()

        else:
            print('token [{}] is invalid'.format(i))
            return None

    return eTree

"""
Evaluate parsetree,this function should take a binary tree as input and should 
return True or False that is based on the on the input statement
"""
def evaluateMPLogicParseTree(t):
    opers = {'AND': operator.iand, 'OR': operator.ior}

    leftC = t.getLeftChild()
    rightC = t.getRightChild()

    rootVal = t.getRootVal()

    if leftC and rightC:
        fn = opers[rootVal]
        return fn(calculate(evaluateMPLogicParseTree(leftC)), calculate(evaluateMPLogicParseTree(rightC)))
    else:
        return rootVal

"""
this function should take a binary tree as input and should 
return the string that looks like the original string 
"""
def printMPLogicExpression(t):
    sVal = ''
    if t:
        sVal = '(' + printMPLogicExpression(t.getLeftChild())

        rootVal = t.getRootVal()
        if type(rootVal) is bool:
            if rootVal:
                rootVal = 'T'
            else:
                rootVal = 'F'

        if type(rootVal) is float:
            if rootVal >= 0.75:
                rootVal = 'P_' + str(rootVal)
            else:
                rootVal = 'M_' + str(rootVal)

        sVal = sVal + rootVal
        sVal = sVal + printMPLogicExpression(t.getRightChild())+')'
    return sVal

""" 
    unit tests concluding whether different areas of t
    he program operate correctly 
    """
class TestMPLogicParseTreeFunction(unittest.TestCase):
    
    def test_buildMPLogicParseTree_InvalidProbably(self):
        self.assertEqual(
                buildMPLogicParseTree('( ( T AND F ) OR P_0.6 )'),
                None, "Should be None")

    def test_buildMPLogicParseTree_InvalidMaybe1(self):
        self.assertEqual(
                buildMPLogicParseTree('( ( T AND F ) OR M_0.9 )'),
                None, "Should be None")

    def test_buildMPLogicParseTree_InvalidMaybe2(self):
        self.assertEqual(
                buildMPLogicParseTree('( M_0.9 )'),
                None, "Should be None")

    def test_buildMPLogicParseTree_ReturnBinaryTree(self):
        self.assertIsInstance(
                buildMPLogicParseTree('( ( T AND F ) OR M_0.3 )'),
                BinaryTree, "Object should be of type BinaryTree")

    def test_evaluateMPLogicParseTree_T_AND_F(self):
        pt = buildMPLogicParseTree('( T AND F )')
        self.assertEqual(
                evaluateMPLogicParseTree(pt), False, "Should be False")

    def test_evaluateMPLogicParseTree_T_OR_F(self):
        pt = buildMPLogicParseTree('( T OR F )')
        self.assertEqual(
                evaluateMPLogicParseTree(pt), True, "Should be True")

    def test_printMPLogicExpression1(self):
        result = '(((P_0.8)AND(T))OR(M_0.25))'
        pt = buildMPLogicParseTree('( ( P_0.8 AND T ) OR M_0.25 )')
        self.assertEqual(printMPLogicExpression(pt), result, "Expression does not match")

    def test_printMPLogicExpression2(self):
        result = '((M_0.7))'
        pt = buildMPLogicParseTree('( M_0.7 )')
        self.assertEqual(printMPLogicExpression(pt), result, "Expression does not match")


"""
code to run when exectuted as a standalone program 
"""
def main():
    print('*' * 45)
    pt = buildMPLogicParseTree('( ( T AND F ) OR M_0.3 )')
    print('pt: ', pt)
    ans = evaluateMPLogicParseTree(pt)
    print('ans: ', ans)
    exp = printMPLogicExpression(pt)
    print('exp: ', exp)

    print('*' * 45)
    pt = buildMPLogicParseTree('( ( T AND F ) OR P_0.9 )')
    print('pt: ', pt)
    ans = evaluateMPLogicParseTree(pt)
    print('ans: ', ans)
    exp = printMPLogicExpression(pt)
    print('exp: ', exp)

    print('*' * 45)
    """
    Caveat: Modified to remove the parenthesis around M_0.25 which incorrectly parses
    """
    pt = buildMPLogicParseTree('( ( P_0.8 AND T ) OR M_0.25 )')
    print('pt: ', pt)
    ans = evaluateMPLogicParseTree(pt)
    print('ans: ', ans)
    exp = printMPLogicExpression(pt)
    print('exp: ', exp)

    """
    single probability expression gets pushed to stack then popped - DOES NOT WORK
    """
    print('*' * 45)
    pt = buildMPLogicParseTree('( M_0.7 )')
    print('pt: ', pt)
    ans = evaluateMPLogicParseTree(pt)
    print('ans: ', ans)
    exp = printMPLogicExpression(pt)
    print('exp: ', exp)


"""
unittest_main() - run unittest's main, which runs TestMPLogicParseTreeFunction's methods
"""
def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main(verbosity=2)

"""
evaluates to true if run as standalone program (e.g. $ python hashtable.py)
"""
if __name__ == '__main__':
    main()
    unittest_main()
