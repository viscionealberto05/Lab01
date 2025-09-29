from random import randint

def stampa_griglia(n, pos, uscita):
    """Stampa la griglia con G = giocatore, U = uscita, . = spazio vuoto"""
    # TODO
    for r in range(0,n):
        for c in range(0,n):
            if r == pos[0] and c == pos[1]:
                print("G", end="")
            elif r == n-1 and c ==n-1:
                print("U", end="")
            else:
                print(".", end="")
        print()

def muovi(pos, mossa):
    """Aggiorna la posizione in base alla mossa"""
    # TODO
    if(mossa == 'n'):
        pos[0] = pos[0]-1
    if(mossa == 'n'):
        pos[0] = pos[0]+1
    if(mossa == 'e'):
        pos[1] = pos[1]+1
    if(mossa == 'o'):
        pos[1] = pos[1]-1
    return pos


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

    # TODO
    x = randint(0, n-1)
    y = randint(0, n-1)

    posizione = [x, y]

    print(f"Livello {livello} Griglia {n}x{n}")

    finito = False
    uscita = False

    while not finito:
        stampa_griglia(n, posizione, uscita)

        print("Mossa (n/s/e/o): ", end="")
        mossaLetta = input()
        posizione = muovi(posizione, mossaLetta)
        if(posizione[0] == n-1 and posizione[1] == n-1):
            uscita = True
            finito = True
        if(posizione[0]<0 or posizione[0]>n-1 or posizione[1]<0 or posizione[1]>n-1):
            uscita = False
            finito = True

        if(uscita == True):
            print("Hai raggiunto l'uscita!")
            return True
        else:
            print("GAMEOVER: Sei uscito dalla griglia!")
            return False

def main():
    print("=== Benvenuto in Room Escape ===")
    livello = 0
    max_livello = 5

    while livello <= max_livello:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break


if __name__ == "__main__":
    main()
