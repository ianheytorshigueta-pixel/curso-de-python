"""Escreva um programa que leia um valor em metros e o
exiba convertido em centímetros e milímetros"""

m = float(input("Informe uma medida em metros: "))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print(f"A medida de {m:.1f}m corresponde a"
      f"\n{km}km"
      f"\n{hm}hm"
      f"\n{dam}dam"
      f"\n{dm:.0f}dm"
      f"\n{cm:.0f}cm"
      f"\n{mm:.0f}mm")
