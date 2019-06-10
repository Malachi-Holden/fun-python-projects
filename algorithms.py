"""
Various algorithms I've written for class projects and for fun
"""

import time
import sys
import math

def shortest_distance(a):
    """
    Brute force algorithm for computing the shortest absolute value between pairs of points in an array.
    a is a list of numbers. 'distance' means absolute value
    Computes in O(n^2) time
    """
    dmin = abs(a[0]-a[1])
    for i in range(len(a)):
        for j in range(len(a)):
            if (i!=j) and (abs(a[i] - a[j]) < dmin):
                dmin = abs(a[i] - a[j])
    return dmin

def mergesort(a):
    """
    Sorts the list a using mergesort
    """
    n = len(a)
    if n == 1:
        return a
    else:
        first = mergesort(a[:n//2])
        second = mergesort(a[n//2:])
        return merge(first, second)

def merge(a, b):
    """
    merges the lists a, b for use in merge sort
    """
    i = 0
    j = 0
    result = []
    while True:
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
        if i == len(a):
            result += b[j:]
            break
        if j == len(b):
            result += a[i:]
            break
    return result

def shortest_distance2(a):
    """
    finds the shortest distance between pairs of numbers in list a
    sorts the list first and then finds the shortest distance
    complexity: O(nlogn)
    """
    a = sort(a)
    dmin = abs(a[0]-a[1])
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1]) < dmin:
            dmin = abs(a[i]-a[i+1])
    return dmin


def reverse(a):
    """
    a is a string. Returns the reverse of a, which is a backwards
    """
    b = ''
    for i in range(len(a)-1,-1,-1):
        b+=a[i]

    return b

def is_palindrome(a):
    """
    Tells whether a is itself backwards
    """
    return a==reverse(a)

def power(x, y):
    """
    returns x^y
    """
    if y == 0:
        return 1
    if y == 1:
        return x
    if y < 0:
        return 1/(power(x, -y))
    else:
        r = y%2
        p = power(x, y//2)
        return p*p*power(x, r)

def permutation(n, k):
    """
    calculates n!/k!
    """
    prod = 1
    for i in range(k+1, n+1):
        prod *= i
    return prod


def factorial(n):
    """calculates n!"""
    return permutation(n, 1)

def combination(n,k):
    return permutation(n,n-k)//factorial(k)

def tiling(n):
    """calculates the n+1th fibbanocci number"""
    phi = (1+math.sqrt(5))/2
    psi = (1-math.sqrt(5))/2
    return int((phi**(n+1) - psi**(n+1))/math.sqrt(5))

def choose_items(array, k):
    """returns a list of all subsets of size k from array
    assumes k<array.length. The items of array should be distinct"""
    if k==1:
        return [[item] for item in array]
    #___________

    result = []
    for i in range(len(array)):

        result += [item + [array[i]] for item in choose_items(array[i+1:], k-1)]

    return result

def powerset(array):
    """returns a list of all subsets of array. The items of array should be distinct"""
    if not array:
        return [[]] #array is empty
    #else
    a = powerset(array[1:])
    result = []
    for item in a:
        result.append(item)
        result.append([array[0]]+item)
    return result



def partitionproblem(array):
    """
    brute force solution to partition problem
    given array of positive integers,
    partitions into two disjoint sets whose sum is the same
    """
    subsets = powerset(array)
    S = set(array) #convert into set for easy subtraction
    for sub in subsets:
        compliment = list(S - set(sub))
        if sum(sub) == sum(compliment):
            return sub, compliment

    return None #explicit


def cliqueproblem(graph, k):
    """
    brute force solution to cliqueproblem
    tell if graph has a clique (complete subgraph) of order k
    graph is represented as a boolean adjacency matrix
    """
    if k == 0:
        return True
    if k==1:
        return len(graph) > 0

    n = len(graph)
    a = choose_items(range(n), k) #//thinking of each vertex as being a number from 0 to n, gives all subsets of n of size k

    for sub in a:
        is_clique = True
        for i in sub:
            for j in sub:
                if (not graph[i][j]) and (j!=i):
                    print(i, j)
                    is_clique = False
                    break
            if not is_clique:
                break
        if is_clique:
            return True

    return False


def logint(num, base):
    """
    returns the largest integer x such that base^x <=num
    num and base should be integers
    """
    result = 0
    while num > 0:
        result += 1
        num = num//base
    return result -1





if __name__ == '__main__':
    for n in range(100):
        x = combination(2*n, n)
        y = 4**n
        print(x,y)
        print(x<y)
