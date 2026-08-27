def rotr(x, n):
    """Rotacja 32-bitowej liczby x w prawo o n pozycji."""
    # Obcinamy x do 32 bitów na wypadek, gdyby wejście było większe
    x = x & 0xFFFFFFFF
    
    # Przesuwamy biny w prawo o 'n' OR przesuwamy w lewo o '32-n' i nakładamy maskę
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

text = input(": ")
ascii = [ord(znak) for znak in text]
ascii = ascii + [(16-len(ascii))]*(16-len(ascii))
S = [1,3,4,7,9,2,5,6,10,8,11,12,16,15,13,14]

D = [x%10 for x in ascii]



wynik = [S[x] for x in D]

L=0
i = 0
while (i < 98):
    ascii = ascii[1:] + ascii[:1]
    ascii = [x+ascii[0] for x in ascii]
    ascii = ascii[2:] + ascii[:2]
    i = i+1
    A = [x + y for x,y in zip(D,ascii)]
    B = [L*i + y for y in wynik] 
    ascii = [x*y for x,y in zip(A,B)]
    ascii = ascii[3:] + ascii[:3]
    ascii = [x*ascii[0] for x in ascii]
    ascii = [rotr(x,5) for x in ascii]
    ascii = [x ^ L for x in ascii]
    L = L%16
    L = S[L]
    baza = ascii[:16]
    reszta = ascii[16:]
    for idx, wartosc in enumerate(reszta):
        baza[idx % 16] += wartosc
    ascii = baza

    ascii = [x%127 for x in ascii]
    

final_state = ascii
print(ascii)
# 1. Zamiana każdej liczby na pojedynczy znak
#znaki = [chr(kod) for kod in ascii]

# 2. Sklejenie listy znaków w jeden tekst (ciąg znaków)
#final_state = "".join(znaki)



znaki_alfanumeryczne = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"
skrot_znaki = []
for x in final_state:
    # Używamy modulo do bezpiecznego wyboru znaku z puli bezpiecznych znaków
    skrot_znaki.append(znaki_alfanumeryczne[x % len(znaki_alfanumeryczne)])

tekst_ = "".join(skrot_znaki)

print("Wyjściowy tekst:", tekst_)

    




