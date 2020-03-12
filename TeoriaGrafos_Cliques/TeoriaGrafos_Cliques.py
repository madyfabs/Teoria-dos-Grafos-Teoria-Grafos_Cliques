class Node (object):

    def __init__(self, name):
        self.name = name
        self.vizinhos = []

    def __repr__(self):
        return self.name


A = Node('1')
B = Node('2')
C = Node('3')
D = Node('4')
E = Node('5')


A.vizinhos = [2, 3, 5]
B.vizinhos = [1, 3]
C.vizinhos = [1, 2, 4]
D.vizinhos = [3, 5]
E.vizinhos = [1, 4]


listaNos = [A, B, C, D, E]


def busca_cliques (cliqueProva=[], noResto=[], pulaNo=[], profundidade=0):

    if len(noResto) == 0 and len(pulaNo) == 0:
        print('This is a clique:', cliqueProva)
        return 1

    totalCliques = 0

    for node in noResto:

        new_cliqueProva = cliqueProva + [node]
        new_noResto = [n for n in noResto if n in node.vizinhos]
        new_skip_list = [n for n in pulaNo if n in node.vizinhos]
        totalCliques += busca_cliques(new_cliqueProva, new_noResto, new_skip_list, profundidade + 1)

        
        noResto.remove(node)
        pulaNo.append(node)
    return totalCliques

totalCliques = busca_cliques(noResto= listaNos)
print('Total cliques found:', totalCliques)
