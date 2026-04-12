import pickle

f = open("Studentdata.dat", "rb")
datas = pickle.load(f)
f.close()

c = 'y'
while c == 'y':

    while True:
        name = input("Student Name: ")
        reg = input("Register No: ")

        found = False
        for i in datas:
            if i[1] == reg:
                found = True
                break

        if found:
            print("Register Number Already Exists. Please enter again.")
            print()
        else:
            break

    l = []
    l.append(name)
    l.append(reg)
    l.append(int(input("Tamil     : ")))
    l.append(int(input("English   : ")))
    l.append(int(input("Maths     : ")))
    l.append(int(input("Physics   : ")))
    l.append(int(input("Chemistry : ")))
    l.append(int(input("Biology   : ")))
    datas.append(l)
    print("Student Record Added Successfully.")

    print()
    c = input("Any More Students (y/n): ").lower()

f = open("Studentdata.dat", "wb")
pickle.dump(datas, f)
f.close()