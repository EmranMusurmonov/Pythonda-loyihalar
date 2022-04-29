# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:19:59 2022

@author: Emran
"""
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
 
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")


sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)


sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)


t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']


print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")


friends = []
friends.append('John')
friends.append('Alex') 
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)


friends.remove('John')
friends.remove('Alex')
print(friends)


friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)


mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)