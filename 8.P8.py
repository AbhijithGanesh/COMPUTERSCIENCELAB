#sum of elements

def sum(x):
    if type(x) == list:
        raise TypeError
    else:
        output = 0
        for i in range(x) :
            if type(i) != int:
                raise TypeError
            output += i
    print(output)
    
    
sum(10)
