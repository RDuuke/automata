from afnd_automata import afnd_automata


if __name__ == "__main__":
    print("Agrega los estados separados por una coma (,)")
    q = input()
    states = q.split(",")
    print("Agrega los simbolos de entrada separados por una coma (,)")
    e = input()
    alphabet = e.split(",")
    print("Agrega el estado inicial")
    q0 = input()
    print("Agrega los estados finales separados por una coma (,)")
    f = input()
    final = f.split(",")
    afnd = afnd_automata(states, alphabet, q0, final)
    afnd.generateTable()
    #afnd.printTable()
    print("¿Es AFND?")
    print(afnd.isafnd)
    afnd.drawAFND()
    afnd.convertToAFN()
    afnd.drawAFN()
    #afnd.draw()
