# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:34:59 2024

@author: Bich Dao
"""

a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Đây là tam giác đều.")
    elif a==b or b==c or c==a:
        print("Đây là tam giác cân")
    elif a**2 + b**2 ==c**2 or a**2 +c**2 == b**2 or b**2+c**2 ==a**2:
        print("Đây là tam giác vuông cân")
    else : 
        print("Không phải ba cạnh của tam giác")

    
    
    
 
