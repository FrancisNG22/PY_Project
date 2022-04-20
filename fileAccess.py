#f = open("mycontact.txt")
#print(f)

#f = open("mycontact.txt", 'w')
#f = open("README.md",'r+b')

#f = open("mycontact.txt", 'w', encoding='utf-8')
#rint(f)

#f.close()
import fnmatch
import os

try:
    f = open("mycontact.txt",encoding='utf-8')
    temp = f.readlines()
#    print(f.readlines())
#    print(temp)
    print(temp[0])
    print(temp[1])
    print(temp[2])

    stemp = temp[0].split("\t")
    print(stemp[0])
    print(stemp[1])

    print(os.getcwd())

    for file in os.listdir('.'):
        if file.endswith(".txt"):
            print(file)
        if fnmatch.fnmatch(file,"*.txt"):
            print(file)

#except:
except Exception as e:
#    print("error")
    print(e)
finally:
    f.close()





