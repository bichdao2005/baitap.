# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:02:58 2024

@author: Bich Dao
"""

a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
denta=b*b-4*a*c
if denta<0:
    print(" Phương trình vô nghiệm.")
elif denta==0:
    print("Phương trình có nghiệm kép")
    print("x= ", -b/2*a)
else:
    print("Phương trình có 2 nghiệm phân biệt.")
        x1 = (-b + math.sqrt(denta))/(2*a)
        x2 = (-b - math.sqrt(denta))/(2*a)
    print("x1=",x1)
    print("x2=",x2)


             