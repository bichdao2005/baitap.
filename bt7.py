# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:44:03 2024

@author: Bich Dao
"""

a=float(input("Nhập giá trị của a: "))
b=float(input("Nhập giá trị của b: "))
if a !=0:
    x =-b/a
    print("Phương trình có nghiệm là :",x)
elif a==0 and b==0:
        print("Phương trình có vô số nghiệm.")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm.")
        
