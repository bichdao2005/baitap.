# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:05:14 2024

@author: Bich Dao
"""
discount=0,92
a=float(input("Nhập quãng đường đi được (km)"))
if a<=1:
    st=20000
    print("số tiền phải trả là",st)
elif  a<=3:
    st=13000*a
    print("số tiền phải trả là ", st)
elif a>=4 and a<=8:
    st= a*13000+(a-3)*12000
    print("số tiền phải trả là ",st)
elif a>8:
    st=13000*a+(a-3)*10000
    print("số tiền phải trả là",st)
    if st>100000:
        tt = st*discount
    print("Tổng số tiền là",tt)
          
         
     
    
    