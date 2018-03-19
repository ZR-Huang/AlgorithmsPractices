# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:39:55 2018

@author: ZR-Huang
function:
    multiply two big integer through the Karatsuda Algorithm

Request:
    1. the number of the digits of two integer needs to be the power of 2, 
    2. the length of two integer need to be equal.
"""
def GetNumberLength(x):
    length = 0
    while(True):
        if x == 0:
            break
        x = int(x/10)
        length +=1
    return length

def Karatsuda(x,y):
    lengthX = GetNumberLength(x)
    #lengthY = GetNumberLength(y)
    if(lengthX == 4):
        return x*y
    a = int(x / (10 ** int(lengthX/2)))
    b = int(x % (10 ** int(lengthX/2)))
    c = int(y / (10 ** int(lengthX/2)))
    d = int(y % (10 ** int(lengthX/2)))
    ac = Karatsuda(a,c)
    bd = Karatsuda(b,d)
    a_plus_b_mul_c_plus_d = Karatsuda((a+b),(c+d))
    ad_plus_bc = a_plus_b_mul_c_plus_d - ac - bd
    result = (10 ** lengthX)*ac + (10 ** int(lengthX/2))*ad_plus_bc + bd
    return result


# test
x = 12345678
y = 87654321
if(Karatsuda(x,y) == 1082152022374638):
    print("success")
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    #if(Karatsuda(x,y) == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184):
      #  print("success")

