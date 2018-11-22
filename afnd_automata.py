import graphviz as gv

class afnd_automata:
    Q = []
    E = []
    Qo = []
    F = []
    TableAFNDdraw = []
    TableAFNdraw = []
    headers = ["Estados"]
    flag = False
    TableAFND = {}
    TableAFN = {}

    def __init__(self, q, e, Qo, F):
        self.Q = q
        self.E = e
        self.Qo = Qo
        self.F = F

    def generateTable(self):

        for q in range(0, len(self.Q)):
            self.TableAFND[self.Q[q]] = {}
            for e in range(0, len(self.E)):
                print("Agrega la transicion del estado [" + self.Q[q] + "] para el simbolo [" + self.E[
                    e] + "]. nota: si son dos estados serpararlos por #")
                state = input()
                self.addAFNDTransition(self.Q[q], self.E[e], state)
                if state.find("#") != -1:
                    states = state.split("#")
                    self.addTransitionAFNDDraw(self.Q[q], states[0], self.E[e])
                    self.addTransitionAFNDDraw(self.Q[q], states[1], self.E[e])
                    self.flag = True
                    continue
                elif state.find("-") != -1:
                    self.flag = True
                    continue
                else:
                    self.addTransitionAFNDDraw(self.Q[q], state, self.E[e])

    def printTable(self):
        table = "______________________\n"
        table = table + "|ESTADOS|"
        for e in self.E:
            table = table + "    %s    |" % e
        table = table + "\n"
        for t in self.TableAFND.keys():
            table = table + "|   " + t + "  |   " + self.TableAFND[t]['a'] + "   |   " + self.TableAFND[t][
                'b'] + "   |\n"

        print(table)

    @property
    def isafnd(self):
        return "Sí" if self.flag else "No"

    def draw(self, table, name):
        g = gv.Digraph(format="png", name=name)
        g.graph_attr["rankdir"] = "LR"
        g.node("ini", shape="point")
        for e in self.Q:
            if e in self.F:
                g.node(e, shape="doublecircle")
            else:
                g.node(e)
            if e == self.Qo:
                g.edge("ini", e)

        for t in table:
            if t[2] not in self.E:
                return 0
            g.edge(t[0], t[1], label=str(t[2]))
        g.render(view=True)

    def convertToAFN(self):
        states = list(self.TableAFND.keys())[0]
        self.loop(str(states))

    def loop(self, state_in):
        if state_in == "-":
            return True
        if not self.existAFN(state_in):
            self.addState(state_in)
            for a in self.E:
                if state_in.find("#") != -1:
                    t = []
                    for s in state_in.split("#"):
                        n = str(self.getTransition(s, a))
                        if any(n in string for string in t):
                            continue
                        elif n == "-":
                            continue
                        else:
                            t.append(n)
                    f = "#" . join(t)
                    self.addAFNTransition(state_in, a, f)
                    self.addTransitionAFNDraw(state_in, f, a)
                    self.loop(f)
                elif state_in == "-":
                    return True
                else:
                    if self.getTransition(state_in, a) == "-":
                        continue
                    else:
                        self.addAFNTransition(state_in, a, self.getTransition(state_in, a))
                        self.addTransitionAFNDraw(state_in, self.getTransition(state_in, a), a)
                        self.loop(self.getTransition(state_in, a))
        else:
            return True

    def addTransitionAFNDraw(self, q, e, transition):
        self.TableAFNdraw.append((q, e, transition))

    def addTransitionAFNDDraw(self, q, e, transition):
        self.TableAFNDdraw.append((q, e, transition))

    def getTransition(self, state, alphabet):
        return str(self.TableAFND[state][alphabet])

    def drawAFN(self):
        self.draw(self.TableAFNdraw, "AFN")

    def drawAFND(self):
        self.draw(self.TableAFNDdraw, "AFND")

    def existAFN(self, state):
        return state in self.TableAFN

    def addState(self, state):
        self.TableAFN[state] = {}

    def addAFNTransition(self, state_in, aphabet, state_go):
        self.TableAFN[state_in].update({aphabet : state_go})

    def addAFNDTransition(self, state_in, aphabet, state_go):
        self.TableAFND[state_in].update({aphabet : state_go})