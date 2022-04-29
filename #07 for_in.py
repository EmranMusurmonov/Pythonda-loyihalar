# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:25:30 2022

@author: Emran
"""

ismlar = ['Ali','Vali','Hasan','Husan','Olim']
for ism in ismlar:
    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")


print(f"Kod {len(ismlar)} marta takrorlandi")


sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)

kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)    


n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)