'''
Given an string, reverse it by using a stack
 '''


class Stack:
    def __init__(self):
        self.stack = []
        self.top = len(self.stack)+1

    def peek(self):
        if self.isEmpty():
            return
        return self.stack[self.top]


    def push(self, data):
        self.stack.append(data)


    def pop(self):
        if self.isEmpty():
            return
        return self.stack.pop()

    def isEmpty(self):
        if self.top < 0:
            return True
        return False



def reverse_string_using_stack(str):
    ''' we're using a stack to reverse the string '''
    reversed_string = ''
    if not str:
        return
    new_stack = Stack()
    str_arr = str.split()
    for i in range(len(str_arr)):
        new_stack.push(str_arr[i])

    for i in range(len(str_arr)):
        reversed_string += new_stack.pop()
        print('reversed string  iterations = ' + reversed_string)

    return reversed_string




a_string = 'abcd'

print(reverse_string_using_stack(a_string))
    
    

    