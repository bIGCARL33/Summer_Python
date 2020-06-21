import math
Name= input("Name")
G1=float(input("Exam 1"))
G2=float(input("Exam 2"))
G3=float(input("Exam 3"))
g_avg=(int(G1)+int(G2)+int(G3))/3
if g_avg<=100 and math.ceil(g_avg+.00000001)>=90:
    print("Grade=A")
elif math.ceil(g_avg+.00000001)<90 and math.ceil(g_avg+.00000001)>=80:
    print("Grade=B")
elif math.ceil(g_avg+.00000001)<80 and math.ceil(g_avg+.00000001)>=70:
    print("Grade=C")
elif math.ceil(g_avg+.00000001)<70 and math.ceil(g_avg+.00000001)>=60:
    print("Grade=D")
elif math.ceil(g_avg+.00000001)<60:
    print("Status=Fail Mother Fucker")
print("Numierical Grade=",math.ceil(g_avg+.000000001),"%")














