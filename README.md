matn kiritiladi. kiritilgan matndan har bitta so'zlarni olib orqadan bitta bittadan harfni ajratib, so'zning qolgan qismidan bazada so'z asosi bormikna yoki yoqligini tekshirish kerak. 

har bitta so'z asosini kichkina harf qilib tekshirish kerak. 
```python
def asos_uchun(matn):
    sozlar = matn.split()
    for soz in sozlar:
        if soz[-1] in ['.',',','!','?']:
            soz = soz[:-1]
        if soz.lower() in asoslar:
            print(f"{soz} so'zi asosli")
        else:
            print(f"{soz} so'zi asosli emas")
matn = input("Matn kiriting: ")
asoslar = ['kitob','qalam','ruchka','olma','banan']
asos_uchun(matn)
```
# Natija
```
Matn kiriting: kitob, qalam, ruchka, olma, banan
kitob so'zi asosli
qalam so'zi asosli
ruchka so'zi asosli
olma so'zi asosli
banan so'zi asosli
```
# Masala

# Masala
# Masala
