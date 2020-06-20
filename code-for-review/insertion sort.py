# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:19:43 2020

@author: heitk
"""

list = [21, 5, 22, 20, 12, 3, 11, 5, 13, 16]

def insertion_help(list, ele):
    x=0
    if len(list) == 0:
      list.insert(x, ele)
    else:
        while list[x]<ele:
            x=x+1
            if x==len(list):
                list.insert(x+1, ele)
                return list

        list.insert(x, ele)
    return list

insertion_help(list, 7)




def insertion_sort(list):
    liste2=[]

    for x in range(len(list)):
        liste2 = insertion_help(liste2, list[x])

    return liste2


print (list)
print (insertion_sort(list))

