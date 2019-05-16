from bintrees import RBTree
#https://pypi.org/project/bintrees/
#pip install bintrees
import fill_inputdata

"""
 FELADAT:
 Adott egy tömb és egy M szám. Meg kell találni az adott tömb legnagyobb összeggel bíró résztömbjét modulo M.
 BEMENET:
 3 sor: -teszteset száma
        -tömb méret és a modulo szám
        -tömb elemei
 KIMENET:
 Egyes tesztesetekre vonatkozó válasz (az összeg)
 ALAPÖTLET:
 Ha egy külön tömbben összegzem az eredeti tömb elemeit 0-tól i-ig (mod m),
 akkor egy adott résztömb összegét j-től i-ig kitudom számolni úgy, hogy:
 result = tömb[i] - tömb[j-1].
 A megoldást megkaphatjuk úgy, hogy ezeknek a result-eknek a maximumát vesszük, de így O(n^2) megoldás lenne
 Ha viszont egy (self-balancing) fában tároljuk az összegző, segédtömb értékeket, akkor egy n darab nodeból álló fát kapunk.
 Így elég lesz csak 1x végig menni a nodeokon (O(n)), és megnézni, hogy mekkora egy adott node és a rákövetkező (log(n)) különbsége, ezek köztül pedig a maximális kell.
 Azért egy node és a rákövetkezőjét kell venni, mert ez a potenciálisan legnagyobb érték. Pl.:
 Ha van egy 4-es érték és egy 5-ös érték, és mi modulo 7 számolunk, akkor 4-5 (mod 7) = 6. (Tehát egy adott érték és a hozzá LEGKÖZELEBBI, de nála NAGYOBB érték kell)
 """
def max_sum_mod(array,size,m):

    sum = [0]*size
    # Első elem létrehozása, ez után ciklus kell
    sum[0] =array[0]%m
    RB = RBTree()
    RB.insert(sum[0],sum[0]) #key, value páros
    result = sum[0]
    for i in range(1,size):
        #flag azért kell, mert implementáció szerint ha egy elemnek nincs rákövetkezője,
        #akkor kivételt dobna

        flag = True
        sum[i] = sum[i-1] + array[i]
        sum[i] %=m

        try:
            (k,v) = RB.ceiling_item(sum[i])    #következő elem
        except KeyError as e:
            #ha nincs rákövetkező akkor nem tudjuk a különbségét venni
            print(e)
            result=max(sum[i], result)
            flag=False
        if flag:
            #pythonban a % művelet negatív számokra is úgy működik, ahogy azt elvárjuk
            #C-ben például a sum[i] -k -hoz hozzá kéne adni az m-et.
            result = max((sum[i] - k )%m, result)
        #ez egy potenciális gyorsítás, ha elértük a maximális értéket (mod m), ami m-1
        #akkor nincs értelme tovább keresni, kiléphetünk a ciklusból
        if result == (m-1):

            break
        RB.insert(sum[i],sum[i])
    #RB.foreach(print, 0)

    return result

def main():

    T = int(input("Hány teszteset legyen? : "))
    fill_inputdata.write_inputs(T)
    #Beolvasás
    with open('inputs.txt' , 'r') as f:
        for i in range(1,T+1):
            l = int(f.readline())
            n, m = [int(x) for x in next(f).split()]
            array = [int(x) for x in next(f).split()]
            result =max_sum_mod(array,n,m)
            print("%d. teszteset eredménye: %li" %(l, result))

if __name__ == "__main__":
    main()
