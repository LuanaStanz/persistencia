import pandas as pd
#ps: vem do cliente o obj, logo não tenho acesso a ele

#caso 1 - erro na formatação esperada!
#alunos_dic = {
#    "nome" : "Jefferson",
#    "curso" : "SI",
#    "IRA" : 4.5
#}

#Isso gera um erro, pois alunos_dic não está formatado como esperado!
#alunos_df = pd.DataFrame(alunos_dic) #erro 
#print(alunos_df)

#caso 2 - formatando o objeto de entrada. Funciona, mas....
#problema: o dev terá que alterar dos dados diretamente!
#caso tenha acesso diretamente a isso é possível
# alunos_dic = {
#    "nome" : ["Jefferson"], #lista de um unico elemento
#    "curso" : ["SI"],
#    "IRA" : [4.5]
#}
#alunos_df = pd.DataFrame(alunos_dic) 
#print(alunos_df)

#caso 3 - alterando todo o objeto de uma vez!
#quando vc não tem acesso aos objetos, envolver dic nos colchetes
alunos_dic = { #obj json vem de uma inface precisso passar p/ dataframe
    "nome" : "Wladimir Tavares",
    "curso" : "CC",
    "IRA" : 7.8
}

# alunos_dic "transformado" em Dataframe
#alunos_df = pd.DataFrame([alunos_dic]) #só envolve.Ls
#print(alunos_df)

##================================================
#persistindo a bade de dados
alunos_csv = pd.read_csv("códigos/aula_04_fastapi/alunos.csv")
#print(alunos_csv)

#Problema: adicionar(persistir) o alunos_dic em alunos_csv
##================================================
#solução 1 - concatenando dois DataFrames!

#concat recebe uma lista de DataFrames!
#alunos_csv = pd.concat([alunos_csv, alunos_df], ignore_index = True) #index = True ignore o index do cara que tá entrando, continue com a contagem original
#print(alunos_csv)
#alunos_csv.to_csv("alunos.csv", index = False) #adiciona coluna do indece. então deixa false se não quiser criar essa nova coluna
##================================================
## outra solução para persistir em csv

#solução 2 - "apendando" o objeto no Dataframe!

#append um novo objeto (linha) ao Dataframe original!
alunos_csv = alunos_csv._append(alunos_dic, ignore_index = True)
print(alunos_csv)
alunos_csv.to_csv("alunos.csv", index = False) #sem index



#testing out
alunos_df_teste = pd.DataFrame(columns = ["id","nome","curso","IRA"])
novo_aluno = {"id":"1","nome":"Jefferson","curso":"SI","IRA":7.6}
novo_aluno_df = pd.DataFrame([novo_aluno])
alunos_df_teste = pd.concat([alunos_df_teste,novo_aluno_df], ignore_index = True)
print(alunos_df_teste)
