import graphviz as gv
import time

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
                print("Agrega la transición del estado [" + self.Q[q] + "] para el símbolo [" + self.E[
                    e] + "]. nota: si son dos estados serpararlos por [#] Ej: q1#q2; y para agregar vacío el símbolo "
                         "[-]")
                state = input()
                if not self.existAFND(state) and state.find("#") == -1 and state.find("-") == -1:
                    print("Estado no válido")
                    time.sleep(3)
                    exit(0)
                else:
                    if state.find("#") != -1:
                        states = state.split("#")
                        for s in states:
                            if not self.existAFND(s):
                                print("Estado no válido")
                                time.sleep(3)
                                exit(0)
                            self.addTransitionAFNDDraw(self.Q[q], s, self.E[e])
                            self.flag = True
                        self.addAFNDTransition(self.Q[q], self.E[e], state)
                        continue
                    elif state.find("-") != -1:
                        self.addAFNDTransition(self.Q[q], self.E[e], state)
                        self.flag = True
                        continue
                    else:
                        self.addAFNDTransition(self.Q[q], self.E[e], state)
                        self.addTransitionAFNDDraw(self.Q[q], state, self.E[e])



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
                    m = False
                    for s in state_in.split("#"):
                        n = str(self.getTransition(s, a))
                        if n.find("#") != -1:
                            for n2 in n.split("#"):
                                if n2 in self.F:
                                    m = True
                                if any(n2 in string for string in t):
                                    n = n.replace(n2, "")
                        else:
                            if n in self.F:
                                m = True
                        n = n.strip("#").lstrip("#")
                        if any(n in string for string in t):
                            continue
                        elif n == "-":
                            continue
                        else:
                            t.append(n)
                    f = "#".join(t)
                    if m:
                        self.F.append(f)
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

    def existAFND(self, state):
        return state in self.Q

    def addState(self, state):
        self.TableAFN[state] = {}

    def addAFNTransition(self, state_in, aphabet, state_go):
        self.TableAFN[state_in].update({aphabet: state_go})

    def addAFNDTransition(self, state_in, aphabet, state_go):
        self.TableAFND[state_in].update({aphabet: state_go})

    def printTransition(self):
        print(self.TableAFND)
        print("------------------------------------------")
        print(self.TableAFN)