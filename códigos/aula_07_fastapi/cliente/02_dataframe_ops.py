import pandas as pd

alunos_df = pd.DataFrame(
    {
        "id": [1,2,3,4,5,6],
        "nome": ["Jefferson", "Wladimir", "Fábio", "Jefferson", "Wladimir", "Fábio"],
        "curso": ["SI", "CC", "ES", "SI", "CC", "ES"],
        "nota": [6.7, 8.3, 3.2, 6.7, 8.3, 3.2]
    }
)

#print(alunos_df)
#print("========")
#print(alunos_df.to_dict(orient="records")) #um objeto por linha
#print(alunos_df.to_dict(orient="records")[0]) #1° obj
#print(alunos_df.to_dict(orient="records")[0].get("nota"))

#obtendo o aluno de id = 2
#print(type(alunos_df["id"] == 2))
#filtro = alunos_df["id"] == 2 #serie de bolleanos
#print(alunos_df[filtro]) #printa linhas que casam com o filtro
#print(type(alunos_df[filtro])) #1, então dataframe? +?
#print(alunos_df[filtro]["nome"].iloc[0]) #coluna, linha

#print(alunos_df["nota"]>6.0) #printa indices + TRUE or False


a_idx = alunos_df.index[ alunos_df["id"] == 2 ]
#print(alunos_df[alunos_df["id"] == 2]) #dataframe
#print(a_idx)
print(type(a_idx)) #pandas.core.indexes.base.Index

#alunos_df.loc[a_idx, ["nota","nome"]] = [8, "Wladimir Tavares"]
#print(alunos_df)
#print(alunos_df.loc[a_idx].to_dict(orient="records")[0])

#print(alunos_df.drop(a_idx).reset_index(drop=True))

#loc: seleção por rotulo(nome)
  #aceita: indices, condições e fatias com nomes de colunas -> df.loc[0:3, ["nome", "curso"]]
#df.loc[0]  # retorna a primeira linha
#df.loc[df["curso"] == "Engenharia"]  # retorna alunos de Engenharia

#iloc: seleção por posição de linhas e colunas. ':' igual a tudo
#df.iloc[0]  # primeira linha
#df.iloc[:, 2]  # terceira coluna de todas as linhas

#drop:  axis=0 remove linha
#       axis=1 remove coluna
#df.drop(2, axis=0)  # remove a linha com índice 2
#df.drop("IRA", axis=1)  # remove a coluna "IRA"
#df.drop([0, 1], axis=0, inplace=True)  # remove as duas primeiras linhas permanentemente