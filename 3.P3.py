#binaryfile

def writer(file):
    import pickle
    students = []
    for i in range(int(input("Enter the number of students"))):
        _name = input("Enter Name")
        _RollNo = int(input("Enter Roll Number"))
        record = [_RollNo, _name]
        students.append(record)
    f = open(file,'wb')
    pickle.dump(students, f)

def search(file):
    import pickle
    file  = open(file, "rb")
    students = pickle.load(file)
    a = int(input("Enter Roll Number"))
    
    for i in students:
        if a == i[0]:
            print("RECORD FOUND")
            print("=============")
            print(i[1],"Is the name of the student")
            print("=============")
            break
    else:
        print("RECORD NOT FOUND")
        print("ERROR")
            

search('Sample.dat')
