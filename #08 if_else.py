# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:37:33 2022

@author: Emran
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car!='gm':
    print(car.title())
  else:
    print(car.upper()) 


login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")


son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")



son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')