# -*- coding: utf-8 -*-

"""
A  --- 85-100 
BA --- 75-84
BB --- 74-60
CB --- 55-59 
CC --- 50-54
FF --- 0-49

Vize, Final
Ortalama= Vize*0,4 + Final*0,6

Ortalamanız = 50 , Harf Notunuz = CC 
"""

def hesapla():
    vizeNotu=float(input("Vize notu gir : "))
    finalNotu=float(input("Final notu gir :"))

#Vize notunun %40 ve Final puanının %60 ını hesaplayalım .

    ortalamaNot=(0.4*vizeNotu)+(0.6*finalNotu)

    print("Not ortalamanız : ",ortalamaNot)

#Koşul kısmına bir de final notunun 50'den büyük olmasını şart koşalım .

    if finalNotu>=50:
    
    
        if(ortalamaNot>=85 and finalNotu>=50):
            print("Harf Notunuz AA")
        elif ortalamaNot>=75 and ortalamaNot<85 :
            print("Harf Notunuz BA")
        elif ortalamaNot >= 70 and ortalamaNot < 75:
            print("Harf Notunuz BB")
        elif ortalamaNot >= 65 and ortalamaNot < 70:
            print("Harf Notunuz CB")
        elif ortalamaNot >= 60 and ortalamaNot < 65:
            print("Harf Notunuz CC")
        elif ortalamaNot >= 55 and ortalamaNot < 60:
            print("Harf Notunuz DC")
        elif ortalamaNot >= 50 and ortalamaNot < 55:
            print("Harf Notunuz DD")

    else:
        print("Harf notunuz FF kaldınız .")

    
hesapla()
  
  
"""
a==b
a>=b
a<=b

0<=x<=49
x>=0 ve x<=49
0<=x
"""    
 
  


    
 
  


    










