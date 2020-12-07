#CSV READER

def CSV_Reader(file):
    import csv
    f = open(file)
    data = csv.reader(f)
    a = int(input("Enter the Roll Number"))
    for i in data :
        if i[0] == a:
            print("The Roll Number is found")
            print("The Name is :" , i[1])
        
def CSV_writer(file):
    import csv
    f = open(file,'w+')
    a = int(input("Enter the Roll Number"))
    b = input("Enter the Name")
    c = int(input("Enter Marks"))
    csv.writer(a,b,c)
    print("The record has been successfully inserted")        
