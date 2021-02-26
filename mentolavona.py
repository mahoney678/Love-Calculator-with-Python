# FLUSWAIR | GITHUB.COM/FSWAIR
import time
a = input("Telefon numaranı giriniz..:")
b = input("Diğer Telefon numarasını giriniz..:")
c = []
for i in a:
  c.append(a[a.index(i)])
for j in b:
  c.append(b[b.index(j)])
for indis in c:
  c[c.index(indis)] = int(c[c.index(indis)])
x = sum(c)
print("Aşk puanınız 50/", int(x / 2), " kere maşallah! & yani %", x)
time.sleep(50)
