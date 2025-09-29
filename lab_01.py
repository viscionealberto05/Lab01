import random
#sol
def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con G = giocatore, U = uscita, . = spazio vuoto"""

    griglia = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(".")
        griglia.append(row)

    
    griglia[n-1][n-1] = "U"


    #pos_x = random.randint(0,n-1)
    #pos_y = random.randint(0,n-1)

    #check = False

    #while check == False:
        #if pos_x != n-1 and pos_y != n-1:
            #griglia[pos_x][pos_y] = "G"
            #check = True
        #else:
            #pos_x = random.randint(0,n-1)
            #pos_y = random.randint(0,n-1)

    #pos = (pos_x,pos_y)

    griglia[pos[0]][pos[1]] = "G"

    return griglia

def muovi(griglia, pos, mossa):
    """Aggiorna la posizione in base alla mossa"""

    moves = ["n","s","e","o"]
    if mossa not in moves:
        exit("Mossa non valida.")

    griglia[pos[0]][pos[1]] = "."



    if mossa == "n":
        pos[0]-=1
        
    elif mossa == "s":
        pos[0]+=1
        
    elif mossa == "e":
        pos[1]+=1
        
    elif mossa == "o":
        pos[1]-=1
        

    print(pos)

    lun = len(griglia)
    
    if pos[0]<0 or pos[1]<0:
        print("sconfinamento")
    elif pos[0]>=lun or pos[1]>=lun:
        print("sconfinamento")
    else:
        griglia[pos[0]][pos[1]] = "G"
    

    for k in range(0,len(griglia)):
        for q in range(0,len(griglia[k])):
            print(f'{griglia[k][q]:5}',end="")
        print("\n")
        

    return griglia



    # TODO

def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco
    Ritorna:
    * True se il giocatore raggiunge l'uscita
    * False se il giocatore va oltre i limiti della griglia.

    NB: Le funzioni stampa_griglia() e muovi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    n = livello + 2

    uscita = [n - 1, n - 1]  # posizione uscita
    pos_x = random.randint(0,n-1)
    pos_y = random.randint(0,n-1)
    

    check = False

    while check == False:
        if pos_x != n-1 and pos_y != n-1:
            #griglia[pos_x][pos_y] = "G"
            check = True
        else:
            pos_x = random.randint(0,n-1)
            pos_y = random.randint(0,n-1)


    pos = [pos_x,pos_y]

    griglia = stampa_griglia(n,pos,uscita)
    
    print("\nLa griglia iniziale è: \n")
    
    #for i in range(len(griglia)):
        #print(griglia[i])

    for k in range(0,len(griglia)):
        for q in range(0,len(griglia[k])):
            print(f'{griglia[k][q]:5}',end="")
        print("\n")

    vittoria = False
    fuorigioco = False

    while vittoria == False and fuorigioco == False:
        
        mossa = str(input("Inserire comando direzione (n,s,e,o): ")) 
        griglia = muovi(griglia,pos,mossa)

        #WinCondition

        if griglia[n-1][n-1] == "G":
            vittoria = True
            print(f"Livello {n-1} superato!")
        
        #OffsideCondition

        flag = 0
        for j in range(0,n):
            if "G" not in griglia[j]:
                flag += 1
        if flag == n:
            fuorigioco = True
            print("Il giocatore ha sconfinato, fine del gioco.")
            

    if vittoria == True:
        return True
    elif fuorigioco == True:
        exit()

    return True
        
        

def main():
    print("=== Benvenuto in Room Escape ===")
    livello = 0
    max_livello = 5

    while livello < max_livello:
        completato = gestisci_livello(livello)
        if completato == True: #condizione di verifica = TRUE oppure no
            livello += 1
        else:
            exit()


if __name__ == "__main__":
    main()
