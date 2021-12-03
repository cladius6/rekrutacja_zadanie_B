import sys

if __name__ == '__main__':
    # liczba słoni
    n = int(input())
    # masa poszczególnych słoni oddzielonych spacją
    m = input().split(' ')
    # numery kolejnych słóni w aktualnym ustawieniu
    a = input().split(' ')
    # numery kolejnych słoni w proponowanym ustawieniu
    b = input().split(' ')
    # By miec pewnosc ze wartosci to liczby
    m = [int(i) for i in m]
    a = [int(i)-1 for i in a]
    b = [int(i)-1 for i in b]

    # masa najlżejszego słonia
    min_m = min(m)
    
    odw = [False] * (n)
    perm = [0] * (n)

    # p(b(i))=a(i) -> Konstrukcja permutacji.
    for i in range(n):
        perm[b[i]] = a[i]
    wynik = 0
    for i in range(n):
        if not odw[i]:
            min_c = sys.maxsize * 2 + 1
            x = i
            c = 0
            suma = 0
            while True:
                min_c = min(min_c, m[x])
                suma += m[x]
                x = perm[x]
                odw[x] = True
                c += 1
                if x == i:
                    break
            # koszt(C) = min(metoda1(C), metoda2(C))
            wynik += min((suma+(c-2)*min_c), (suma+min_c+(c+1)*min_m))
    print(wynik)
