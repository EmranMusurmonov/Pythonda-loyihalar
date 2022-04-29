# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:42:20 2022

@author: Emran
"""

Dadam = {'ismi':'utkir jutaev','t_yili':1984,'viloyati':'shaxrisabz'}
ismi = Dadam ['ismi']
t_yili = Dadam ["t_yili"]
viloyati = Dadam ['viloyati']
print(f"Dadamning ismi {Dadam['ismi'].title()}, {t_yili}-yilda, {viloyati.title()} viloyatida tug'ilgan")



taomlar = {
   'oyim': 'osh',
    'dadam':'manti',
     'akam':'lavash',
     'ukam':'pizza',
           'kichik ukam':'somsa'
}
taom = taomlar ['oyim']
print(f"Oyimning sevimli taomi bu {taom}")


python_lugati = {
    'float':"O'nlik son",
     'string':"Matn",
      'list':"Ro'yxat",
       'tuple':"O'zgarmas ro'yxat",
        'integer':"Butun son",
          'if':'agar',
            'else':'aks xolda'
           }

kalit = input('Bironbir soz kiriting\n >>>> ')
tarjima = python_lugati.get(kalit)
if tarjima==None:
    print("Bunday soz mavjud emas")
else:
    print(f"{kalit.title()} sozi {tarjima} deb tarjima qilinadi")



















