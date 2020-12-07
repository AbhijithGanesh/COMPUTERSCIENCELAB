#separate words by #
def foo(file):
    f = open(file)
    lines = list(f.read())
    for i in range(len(lines)):
        if  lines[i].isspace():
            lines.pop(i)
            lines.insert(i,"#")      
    str1 = ''
    for i in lines:
        str1 += i
    print(str1)
    f.close()

foo("sample.txt")
