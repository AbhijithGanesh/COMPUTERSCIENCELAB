
def convertor(f1,f2):
    file1 = open(f1,"r")
    data  = file1.readlines()
    file1.close()
    file1 = open(f1,"w")
    file2 = open(f2,"w")
    for i in data:
        if "A" or "a" in i:
            file2.write(i)
        else:
            file1.write(i)
    print("The Data has been successfully changed")
convertor("sample.txt","convertor.txt")
