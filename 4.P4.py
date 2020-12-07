#Create a binary file with roll number, name and marks. Input a roll number and update the marks.


def update(file): 
        import pickle
        file = open(file,"rb")
        data = pickle.load(file)
        a = int(input("Enter the roll number"))
        for i in data:
            if a == i[0]:
                b = input("Enter Name")
                c = int(input("Enter Marks"))
                updated_records = [a,b,c]
            else:
                print("The records don't exist")
        file.close()
        f = open(file,"wb+")
        pickle.dump(updated_records, f)
        print("Updated the records")
update("Sample.dat")
