class Calculadora:
    def __init__(self):
        pass

    def dos_proposiciones(self,expresion):
        p = [True, True, False, False]
        q = [True, False, True, False]

        expresion = expresion.replace('p', 'p[i]').replace('q', 'q[i]').replace('xor', '^')
        lista = []
        result = []

        for i in range(4):
            lista.append([p[i], q[i]])
            try:
                lista[i].append(eval(f'{expresion}'))
                result.append(eval(f'{expresion}'))
            except: return "ALGO ANDA MAL...", 0

        return lista,result

    def tres_proposiciones(self, expresion):
        p = [True, True, True, True, False, False, False, False]
        q = [True, True, False, False, True, True, False, False]
        w = [True, False, True, False, True, False, True, False]

        expresion = expresion.replace('p', 'p[i]').replace('q', 'q[i]').replace('xor', '^').replace('w','w[i]')
        lista = []
        result = []
        for i in range(8):
            lista.append([p[i], q[i],w[i]])
            try:
                lista[i].append(eval(f'{expresion}'))
                result.append(eval(f'{expresion}'))
            except:
                return "ALGO ANDA MAL...", 0

        return lista, result

    def formula_bien_formulada(self,lista:list):
        if all(lista):
            return "Tautología"
        elif any(lista):
            return "Contingencia"
        else: return "Contradicción"