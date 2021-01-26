#while input("vuoi che mi fermi? ") != ("si"):
print ("se non rispondi 'no' non mi fermo!")
una_lista_svuota = [1, 2, 3] != [3, 2, 1]  #una lista vuota


string = ("basta Python!") * 1000  #calcolo numeri caratteriri string
print ("la stringa e' lunga", len(string), "caratteri")
print ("A" in string)   

def my_max_of_three(a, b, c): #max fra tre numeri
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

def cerca_vocali(carattere):  #sei vocale o consonante
    vocali = "aeiou"
    if carattere in vocali:
        print('Il carattere ' + carattere + ' è una vocale')
    else:
        print('Il carattere ' + carattere + ' non è una vocale')

def sommatrice(lista):  #sommatrice
    risultato = 0
    for numero in lista:
        risultato += numero
    print('Il risultato della somma è... ' + str(risultato))

#tutti metodi per stringhe
print ("hacking to much time")
a = ("famola maiuscola")
str.upper(a)
print (a)


def moltiplicatore(lista):  #moltiplicatore
    risultato = 1
    for numero in lista:
        if numero != 0:
            risultato *= numero
    print('Il risultato della moltiplicazione tra tutti gli elementi della lista è... ' + str(risultato))

def reverser(stringa):  #reverse
    indice = (len(stringa) -1)
    nuova_stringa = ""
    while indice >= 0:
        nuova_stringa += stringa[indice]
        indice -= 1
    print(nuova_stringa)

def testa_parole(parola):  #palindromo
    indice = (len(parola) -1)
    nuova_parola = ""
    while indice >= 0:
        nuova_parola += parola[indice]
        indice -= 1
    if nuova_parola == parola:
        print('La parola passata è un palindromo! ' + nuova_parola)
    else:
        print('Mi dispiace, la parola inserita non è un palindromo...')

def istogramma(lista):  #istogrammi
    for numero in lista:
        print("*" * numero)

lista = [3,7,9,5]
istogramma(lista)      

def mia_len(lista_o_stringa):  #version lunghezza
    lunghezza = 0
    for unit in lista_o_stringa:
        lunghezza += 1
    print('La Lista o Stringa passata alla funzione ha una lunghezza di ' + str(lunghezza))


mia_len(['asd',2,66,'Roma',3.14])

def contatore(listaA):  #a ciascuno il suo
    listaB = []
    for parola in listaA:
        listaB.append(len(parola))
    print(listaB)

listaA = ['Milano','Roma','Cagliari','Croazia','Giappone']
contatore(listaA)

# oppure una versione più efficiente usando il "list comprehension":
listaA = ['Milano', 'Roma', 'Cagliari', 'Croazia', 'Giappone']
listaB = [len(parola) for parola in listaA]

def max_in_list(lista):  #max fra tutti
    max = 0
    for numero in lista:
        if numero > max:
            max = numero
    print('Il numero più grande della lista passata è ' + str(max))

lista = [9, 33, 1, 3, 2, 4, 22]
max_in_list(lista)

def traduttore():  #linguaggio modificato
    print('''
    Ciao! questo programma traduce un testo passato in "rövarspråket".
    Ció significa che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...
    ''')

    vocali = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"',"'"]
    
    while True:
        testo = input('\nInserisci il testo che desideri tradurre -> ')
        tradotta = ""
        for x in testo:
            if x in vocali or x in specials:
                tradotta += x #tradotta = tradotta + x
            else:
                tradotta = tradotta + x + "o" + x

        print(f"Ecco a te la traduzione! '{tradotta}'")

        if input("\nDesidere tradurre un'altra frase? ") == "no":
            break

def membro_di(char, lista):  #solamente per i soci
    if char in lista:
        print(f"Il carattere '{char}' è presente nella lista passata, all'indice {lista.index(char)}!")
    else:
        print(f"Il carattere '{char}' NON è presente nella lista passata..")

membro_di("x", [2, 3, 4, "x", "z", 7, 1])            

def frequenza_car(stringa):  #frequenzimetro
    mappa = {}
    for carattere in stringa:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    return mappa

def geometra():  #il geometra
    print("""
    Benvenuti alla funzione Geometra!
    A ciascun possibile calcolo corrisponde un valore numerico:
    - Area Quadrato @ 1
    - Area Rettangolo @ 2
    - Area Triangolo @ 3
    - Area Cerchio @ 4
    """)
    
    print('Dunque. Di quale figura geometrica desideri calcolare l\'area?')
    scelta = int(input('=> '))
    if scelta == 1:
        print("Hai scelto: Area Quadrato")
        lato = float(input('Inserisci il valore del lato del quadrato '))
        print(f"L'Area del Quadrato, avente lato {lato} è: {lato * lato}")
    elif scelta == 2:
        print("Hai scelto: Area Rettangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"L'Area del Rettangolo, avente base {base} e altezza {altezza} è: {base * altezza}")
    elif scelta == 3:
        print("Hai scelto: Area Triangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"L'Area del Triangolo, avente base {base} e altezza {altezza} è: {(base * altezza) / 2}")
    elif scelta == 4:
        print("Hai scelto: Area Cerchio")
        r = float(input('Inserisci il valore del raggio '))
        print(f"L'Area del Cerchio, avente raggio {r} è: {(r * r) * 3.14}")
    else:
        print ('Nessun calcolo disponibile per la scelta effettuata!')   


def psw_generator():  #generatore di password
    print('Benvenuti nel generatore di password. Il programma permette di scegliere tra due livelli di complessità della password.')

    full_char_table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    alpha_char_table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    if input("Desideri una password semplice(8 caratteri alfanumerici) o difficile(20 caratteri ascii)?  S/D ") == "D":
        lunghezza = 20
        tipo = full_char_table
    else:
        lunghezza = 8
        tipo = alpha_char_table

    psw = ""
    x = 0

    for x in range(int(lunghezza)):
        psw += tipo[int(random.randrange(len(tipo)))]
        x += 1

    print("La password generata è : " + psw)
       

def fattoriale(n): #func fattoriale
    if n == 1:
        return n
    else:
        result = n * fattoriale(n-1)
        return result       


things = ["Y08501", 0.13, "Q95747", 0.96]
thing  = ["Y08501", 0.13, "Q95747", 0.96]
int(len(thing))
print (len(thing))
thing.append("FUCK")
thing.extend(things)
print (thing)
thing.reverse()
print (thing)
thing.count(things)
print (thing.append(3))

