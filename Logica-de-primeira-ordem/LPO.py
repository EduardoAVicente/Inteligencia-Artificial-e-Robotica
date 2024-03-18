from aima3.logic import expr, FolKB, fol_fc_ask

clauses = []

# Adicionando as cláusulas que você já tem
clauses.append(expr("Progenitor(Maria,Joao)"))
clauses.append(expr("Progenitor(Jose,Joao)"))
clauses.append(expr("Progenitor(Maria,Ana)"))
clauses.append(expr("Progenitor(Jose,Ana)"))
clauses.append(expr("Progenitor(Ana,Felipe)"))
clauses.append(expr("Progenitor(Rufus,Felipe)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(x)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(y)"))
clauses.append(expr("Sexo(Maria,Feminino)"))
clauses.append(expr("Sexo(Joao,Masculino)"))
clauses.append(expr("Sexo(Jose,Masculino)"))
clauses.append(expr("Sexo(Ana,Feminino)"))

clauses.append(expr("Progenitor(x,y) ==> Descendente(y,x)"))

clauses.append(expr("Progenitor(x,y) & Sexo(x,Masculino) ==> Pai(x,y) "))
clauses.append(expr("Progenitor(x,y) & Sexo(x,Feminino) ==> Mae(x,y) "))

clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Masculino) ==> Irmao(y,z)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))

clauses.append(expr("Progenitor(x, y) & Progenitor(z, y) & Sexo(x, Masculino) ==> Avo(y, x)"))

clauses.append(expr("Progenitor(x,y) & Sexo(x,Masculino) & Progenitor(x,z) & Sexo(y,Masculino)==> Tio(z,y)"))


# Criando a base de conhecimento
Genealogia = FolKB(clauses)

# Lista de perguntas
perguntas = ["Sexo(x,Masculino)",
             "Sexo(Maria,x)",
             "Irmao(x,Ana)",
             "Irma(x,Joao)",
             "Descendente(x,Maria)",
             "Descendente(Joao,x)",
             "Pessoa(x)",
             "Mae(x,y)",
             "Pai(x,y)",
             "Avo(x,y)",
             "Tio(Joao,y)"]  

# Fazendo as consultas e imprimindo as respostas
for i in perguntas:
    resposta = fol_fc_ask(Genealogia, expr(i))
    print("%s -> %s" % (i, (list(resposta))))
