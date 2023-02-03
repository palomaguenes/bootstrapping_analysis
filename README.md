[![Python](https://img.shields.io/badge/Python-3.7-blue)]
[![Pandas](hhttps://img.shields.io/badge/Pandas-1.0.3-blue)]
[![Numpy](https://img.shields.io/badge/Numpy-1.17.2-blue)]

# bootstrapping_analysis
Bootstrapping to determine confidence intervals for master thesis propose.

## Executando
Para executar este trabalho, basta colocar no terminal 
``` python bootstrapping.py ```

## Dados de entrada
O arquivo csv em ![exemplo](150respostasExemplo.csv) contém dados simulados parecido com os que serão coletados pelo survey.
O arquivo contém três colunas: 
- id: é o identificador único de uma resposta anonima de um engenheiro de software ao survey.
- ipScore: é a pontuação baseada na escala Clance que determina se a pessoa tem Sindrome do Impostos, que vai de 20 a 100. Esses valores foram calculados aleatoriamente com a função ```ALEATORIOENTRE(20, 100)``` do Excel.
- hasIP: flag calculada baseada no ipScore e no limite definido pela criadora da escala Clance. Quando a pontuação está entre 61 e 80, a pessoa tem sentimentos frequentes da síndrome, quando é maior que 80, os sentimentos além de frequentes são intensos. Sendo assim, quando ipScore é maior que 61, considera-se, neste trabalho, que existe a presença de Síndrome do Impostor.


