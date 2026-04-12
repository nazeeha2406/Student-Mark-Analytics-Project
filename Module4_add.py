import pickle

f=open("Studentdata.dat","rb")
datas=pickle.load(f)
f.close()
f=open("Studentdata.dat","wb")

c='y'
while c=='y':
    l=[]
    l.append(input("Student Name: "))
    l.append(input("Register No: "))
    l.append(int(input("Tamil : ")))
    l.append(int(input("English : ")))
    l.append(int(input("Maths : ")))
    l.append(int(input("Physics : ")))
    l.append(int(input("Chemistry : ")))
    l.append(int(input("Biology : ")))
    datas.append(l)

    c=input("Any More Students: ").lower()

y=pickle.dump(datas,f)
f.close()








