import pickle
f=open("Studentdata.dat","rb")
l=pickle.load(f)

found=0
Regno=input("Register No: ")
print()
for i in l:
    if Regno==i[1]:

        found=True

        print("Student Name: ",i[0])
        print("Register No: ",i[1])
        print()
        print("%8s %8s %8s %8s %10s %8s"%("Tamil","English","Maths","Physics","Chemistry","Biology"))
        print("%8s %8s %8s %8s %10s %8s"%(i[2],i[3],i[4],i[5],i[6],i[7]))
        print()
        print("%8s %8s %8s  %8s  %10s"%("Total","Average","Result","Eng.cut.Off","Medi.cutoff"))

        a=0
        tot=i[2]+i[3]+i[4]+i[5]+i[6]+i[7]
        Avg=tot/6

        if i[2]>=35 and i[3]>=35 and i[4]>=35 and i[5]>=35 and i[6]>=35 and i[7]>=35:
            a="PASS"

        else:
            a="FAIL"

        eng=i[4]+((i[5]+i[6])/2)
        med=((i[5]+i[6])/2)+i[7]

        print("%8d %8.2f %8s %8d %10d"%(tot,Avg,a,eng,med))
        print()
        print("="*60)
    
if not found:
        print("Register Number is Not found in this Table")
f.close()

