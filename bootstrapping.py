# Criado por Paloma Guenes #

import numpy as np
import pandas as pd
import random

#Apresentacao
print("\nEste script calcula o intervalo de confiança baseado na técnica Bootstrapping. \n\n")

#Pegando nome do arquivo de entrada
input_name = input("Escreva o nome do arquivo de entrada ou aperte aperte enter: ")

#Guardando nome do arquivo de entrada default disponibilizado nesta pasta
default_name = 'testes/150respostasExemplo.csv'

#Checando se o arquivo digitado existe, caso nao exista o programa é encerrado
if input_name == "":
  #Lendo o arquivo com dados de exemplo (algo parecido virá do survey)
  print("Lendo o arquivo: " + default_name + "\n\n")
  df = pd.read_csv(default_name)  
else:
  if (input_name[len(input_name) - 4:] == '.CSV' or input_name[len(input_name) - 4:] == '.csv'):
    try:
      with open(input_name, 'r') as f:
          print("Lendo o arquivo: " + input_name + "\n\n")
          df = pd.read_csv(f)
    except IOError:
      print('Arquivo não encontrado!\n\n')
      exit()
  else:
    print('O arquivo não é csv!\n\n')
    exit()
    
#checar se a hasIP existe
if 'hasIP' not in list(df.columns):
  print('O arquivo não contém a coluna hasIP!\n\n')
  exit()

print("Através dos dados lidos, foram encontradas ")

#calculando a porcentagem quando tem IP e quando nao tem
percentage_hasIPTrue = df[df.hasIP == 1].hasIP.count()/150
print(str(round(percentage_hasIPTrue*100, 2)) + "% de pessoas com Sindrome do Impostor")

#lista com o hasIP
list_hasIP = df.hasIP.tolist()

sample_perc = []
#calculo a porcentagem de pessoas com IP em 1000 amostras de tamanho 1000 (com repetição) e guardo na sample_perc
for i in range(1000):
  sample = random.choices(list_hasIP, k=1000)
  mean = np.mean(sample)
  sample_perc.append(mean)

#nivel de confianca do intervalo de confianca 
confidence_level = 0.95

#calculo do intervalo de confianca
confidence_interval = np.percentile(sample_perc,[100*(1-confidence_level)/2,100*(1-(1-confidence_level)/2)]) 
print("com intervalo de confiança de " + str(confidence_interval) +"\n")
