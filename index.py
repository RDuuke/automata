from afnd_automata import afnd_automata
import time

if __name__ == "__main__":
    print("Agrega los estados separados por una coma (,) Ej: q0,q1")
    q = input().replace(" ", "")
    states = q.split(",")
    print("Agrega los símbolos de entrada separados por una coma (,) Ej:1,0")
    e = input().replace(" ", "")
    alphabet = e.split(",")
    print("Agrega el estado inicial.")
    q0 = input().replace(" ", "")
    if not q0 in states:
        print("Estado no válido.")
        time.sleep(3)
        exit(0)
    print("Agrega los estados finales separados por una coma (,) Ej: q0,q1")
    f = input().replace(" ", "")
    final = f.split(",")
    for s in final:
        if not s in states:
            print("Estado no válido")
            time.sleep(3)
            exit(0)

    afnd = afnd_automata(states, alphabet, q0, final)
    afnd.generateTable()
    #afnd.printTable()
    print("¿Es AFND?")
    print(afnd.isafnd)
    afnd.drawAFND()
    afnd.convertToAFN()
    afnd.printTransition()
    afnd.drawAFN()
    #afnd.draw()
