#queue program

def create(*args):
    q = []
    for i in args:
        q.append(i)
    return q

def  pop(q):
    return q[0]

def delete(q):
    return q[0]

def push(q, a):
    return q.append(a)

