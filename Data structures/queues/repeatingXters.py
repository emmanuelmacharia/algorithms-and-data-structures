'''
Problem Description

Given a string A denoting a stream of lowercase alphabets. You have to make new string B.

B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.


Problem Constraints
1 <= length of the string <= 100000


Example Input
Input 1:
 A = "abadbc"

 Input 2:
  A = "abcabc"

Example Output
Output 1:
 "aabbdd"

Output 2:
 "aaabc#"

    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "aba"    -   first non repeating character 'b'
    "abad"   -   first non repeating character 'b'
    "abadb"  -   first non repeating character 'd'
    "abadbc" -   first non repeating character 'd'

'''

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    

class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1


    def enqueue(self, data):
        ''' adds a node to our queue'''
        self.front = 0
        self.rear += 1

        