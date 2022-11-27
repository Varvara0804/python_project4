def ploshad(a, b):
     if(a > 0 and b > 0):
          s = a * b
          return s
     else:
          print(f"Числа должны быть не отрицательными!")

def kvadrat(a):
     y = a * a
     return y

def perimetr(a,b):
     if(a > 0 and b > 0):
          p = (a + b) * 2
          return p
     else:
          print(f"Числа должны быть не отрицательными!")


chislo = int(input("Введите число для возведения в квадрат: "))
res = kvadrat(chislo)
print(f"Квадрат числа {chislo} равен {res}")

dlina = int(input("Введите длину прямоугольника: "))
shirina = int(input("Введите ширину прямоугольника: "))
s = ploshad(dlina, shirina)
p = perimetr(dlina, shirina)
if (s and p):
     print(f"Площадь прямоугольника {dlina} на {shirina} равна {s}, а периметр равен {p}")
