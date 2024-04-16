import itertools
import random

# Funkcje dla szyfrowania tekstu
def generuj_kombinacje_tekst():
    alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    kombinacje = list(itertools.permutations(alfabet, 3))
    kombinacje = [''.join(kombinacja) for kombinacja in kombinacje]
    return kombinacje

def losuj_kombinacje_tekst(kombinacje):
    mieszane_kombinacje = kombinacje[:]
    random.shuffle(mieszane_kombinacje)
    return mieszane_kombinacje

def utworz_klucz_tekst(kombinacje, mieszane_kombinacje):
    return dict(zip(kombinacje, mieszane_kombinacje))

def przygotuj_tekst(tekst):
    znaki_zamiany = ['x', '3', 'b', '1']
    tekst = ''.join(random.choice(znaki_zamiany) if c == ' ' else c for c in tekst)
    while len(tekst) % 3 != 0:
        tekst += 'x'
    return tekst

def szyfruj_tekst(tekst, klucz):
    tekst = przygotuj_tekst(tekst)
    fragmenty = [tekst[i:i+3] for i in range(0, len(tekst), 3)]
    zaszyfrowane_fragmenty = [klucz.get(frag, frag) for frag in fragmenty]
    return ' '.join(zaszyfrowane_fragmenty)

def deszyfruj_tekst(tekst, klucz):
    klucz_odwrotny = {v: k for k, v in klucz.items()}
    fragmenty = tekst.split()
    odszyfrowane_fragmenty = [klucz_odwrotny.get(frag, frag) for frag in fragmenty]
    return ''.join(odszyfrowane_fragmenty)

def przywracanie_spacji(tekst):
    znaki_zamiany = ['x', '3', 'b', '1']
    return ''.join(' ' if c in znaki_zamiany else c for c in tekst)

# Funkcje dla szyfrowania dat
def generuj_kombinacje_dat():
    znaki = ['x', '3', 'b', '1']
    kombinacje = list(itertools.product(znaki, repeat=3))
    kombinacje = [''.join(komb) for komb in kombinacje]
    return kombinacje

def szyfruj_date(data, mapowanie):
    segmenty = data.split('.')
    zaszyfrowana_data = ''
    for segment in segmenty:
        zaszyfrowany_segment = ''.join(mapowanie[int(cyfra)] for cyfra in segment)
        zaszyfrowana_data += zaszyfrowany_segment + '.'
    return zaszyfrowana_data[:-1]

# Wygenerowanie kluczy i przykłady użycia
kombinacje_tekstu = generuj_kombinacje_tekst()
mieszane_kombinacje_tekstu = losuj_kombinacje_tekst(kombinacje_tekstu)
klucz_tekstu = utworz_klucz_tekst(kombinacje_tekstu, mieszane_kombinacje_tekstu)

tekst_do_szyfrowania = "test tekstu do szyfrowania"
print("Tekst do szyfrowania:", tekst_do_szyfrowania)

zaszyfrowany_tekst = szyfruj_tekst(tekst_do_szyfrowania, klucz_tekstu)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)

odszyfrowany_tekst = deszyfruj_tekst(zaszyfrowany_tekst, klucz_tekstu)
tekst_z_przywróconymi_spacjami = przywracanie_spacji(odszyfrowany_tekst)
print("Odszyfrowany tekst:", tekst_z_przywróconymi_spacjami)

kombinacje_dat = generuj_kombinacje_dat()
print("10 pierwszych kombinacji dat:")
for kombinacja in kombinacje_dat[:10]:
    print(kombinacja)

mapowanie_dat = dict(zip(list(range(10)), kombinacje_dat))

data = "13.01.90"
zaszyfrowana_data = szyfruj_date(data, mapowanie_dat)
print("Zaszyfrowana data:", zaszyfrowana_data)
