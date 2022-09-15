import numpy as np #panggil library
from math import e
def my_bisection(f, a, b,iterasi): #fungsi bisection
  if np.sign(f(a)) == np.sign(f(b)): #cek tanda jika sama tidak ada akar pada interval
    raise Exception('Tidak ada akar pada interval a dan b')
  m = b - (f(b) * (b-a))/(f(b)-f(a)) #rumus perbandingan berdasarkan gradien
  if iterasi == 21: #diasumsikan berhenti pada iterasi 16
    print("a = ", a)
    print("b = ", b)
    print("Galat", abs(f(m)))
    return m
  elif np.sign(f(a)) == np.sign(f(m)):
    iterasi +=1
    return my_bisection(f, m, b, iterasi)
  elif np.sign(f(b)) == np.sign(f(m)):
    iterasi +=1
    return my_bisection(f, a, m,iterasi)
#fungsi lambda
f = lambda x : e**x - 5 * (x**2) #mencari fungsi lambda ini
#batas
a = 0
b = 1
print("Maka akar yang ditemukan " ,my_bisection(f,a,b,0))
