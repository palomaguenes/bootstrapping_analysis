import numpy as np
import pandas as pd
import random

#lendo o arquivo com dados de exemplo (algo parecido vira do survey)
df = pd.read_csv('150respostasExemplo.csv')

#calculando a porcentagem quando tem IP e quando nao tem
percentage_hasIPTrue = df[df.hasIP == 1].hasIP.count()/150
print(percentage_hasIPTrue)

percentage_hasIPFalse = df[df.hasIP == 0].hasIP.count()/150
print(percentage_hasIPFalse)

#lista com o hasIP
list_hasIP = df.hasIP.tolist()

#print(list_hasIP)

sample_perc = []
#calculo a porcentagem de pessoas com IP em 1000 amostras de tamanho 1000 (com repetição) e guardo na sample_perc
for i in range(1000):
  sample = random.choices(list_hasIP, k=1000)
  mean = np.mean(sample)
  sample_perc.append(mean)

# print(sample_perc)
# print(np.mean(sample_perc))

#nivel de confianca do intervalo de confianca 
confidence_level = 0.95

#calculo do intervalo de confianca
confidence_interval = np.percentile(sample_perc,[100*(1-confidence_level)/2,100*(1-(1-confidence_level)/2)]) 
print(confidence_interval)
