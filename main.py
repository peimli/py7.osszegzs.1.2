'''
1.2 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!

A program csak a páros számokat adja össze!
'''
import random

l = [random.randint(1,10) for i in range(5)]

l2 = [i for i in l if i % 2 == 0]

i = 0
for k in l2:
  i = i + k

print(l)
print(l2)
print(i)