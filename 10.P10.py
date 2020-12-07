#stack

def create(*args):
    stk = []
    for i in args:
        stk.append(i)
    return stk

def push(stack, x):
    stack.append(x)

def pop(stack):
    stack.pop()

def delete(stack):
    del stack