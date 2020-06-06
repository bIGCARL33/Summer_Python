#Objective of this homework assigment
#- Develop a simple caulator that adds, subtracts, multiplies and divides
#- must also be capable of taking in two inputs from the user by prompting them to input values
import math
print("Welcome to equivalent time Calculator")
print("Input the numerical day in a year (Values 1-365) and the calculator will tell you how inacurate your clock is realtive to the actual time.")
n=float(input("Number day 1-365 EX: Janurary 1= 1 and December 31= 365"))
t= 2*3.1415926*n / 365
#Sin coeffecinets
a1=-7.3412
a2=-9.375
a3=-.3179
a4=-.1739
#Cosine coeffecients
b1=.4944
b2=-3.2568
b3=-.0774
b4=-3.2568
#Sin Terms
as1=math.sin(t)
as2=math.sin(2*t)
as3=math.sin(3*t)
as4=math.sin(4*t)
#Cosine Terms
bc1=math.cos(t)
bc2=math.cos(2*t)
bc3=math.cos(3*t)
bc4=math.cos(4*t)
#Equivalent time equation (Answer is given in Decimal Minutes)
ET=a1*as1+a2*as2+a3*as3+a4*as4+b1*bc1+b2*bc2+b3*bc3+b4*bc4
print(ET)
#Now Lets calculate the solar time
print("Now lets calculate the solar time")
Solar_Time=float(input("Time on computer in Decimal Hours"))+ ET/60+4*(90-float(input("Longitude(97.7431 for Austin)")))/24
print(Solar_Time)
