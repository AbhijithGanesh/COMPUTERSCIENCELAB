def foo (file):
    f = open(file)
    count = f.read()
    vowels = 0
    consonants = 0
    UpperCase = 0
    LowerCase =    0
    for i in count:
        if i.isalpha():
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vowels += 1
            else:
                consonants += 1
    for i in count:
        if i.isupper():
            UpperCase += 1
        elif i.islower():
            LowerCase += 1
        
    print("constants = ",consonants ,"Vowels = ",  vowels,"Upper Case = ",UpperCase,"Lower Case = " , LowerCase, sep= "\n")
 
 
 
foo("Sample.txt")
