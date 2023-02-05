![Python](https://img.shields.io/badge/Python-3.7-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.0.3-blue)
![Numpy](https://img.shields.io/badge/Numpy-1.17.2-blue)

# bootstrapping_analysis
Este projeto é um script que utiliza a técnica de reamostragem Bootstrapping para fornecer intervalos de confiança, auxiliando na amplificação de amostras dos dados para fomentar uma análise mais robusta e acurada.
A documentação mais detalhada pode ser encontrada em [documentação]9https://docs.google.com/document/d/1uUY3nyZEf9qpaAYo15OMJyH44q_eBBOQNeRuc9tfeoo/edit).

## Executando
Para executar este trabalho, basta colocar no terminal 
``` python bootstrapping.py ```
Para rodar o programa com o arquivo de exemplo que foi disponibilizado nesta pasta, basta clicar enter e o programa irá executar.
Caso o usuário queira utilizar uma entrada de dados própria, ela deve:
- ser um arquivo com extensão .csv
- conter uma coluna chamada hasIP, que pode conter o valor 0 ou 1, indicando a ausência ou presença da Síndrome do Impostor, respectivamente, em seus dados.


## Dados de entrada
O arquivo csv em [exemplo](testes/150respostasExemplo.csv) contém dados simulados semelhantes com os que serão coletados pelo survey.
O arquivo contém três colunas: 
- id: é o identificador único de uma resposta anonima de um engenheiro de software ao survey.
- ipScore: é a pontuação baseada na escala Clance que determina se a pessoa tem Síndrome do Impostos, que vai de 20 a 100. Esses valores foram calculados aleatoriamente com a função ```ALEATORIOENTRE(20, 100)``` do Excel.
- hasIP: flag calculada baseada no ipScore e no limite definido pela criadora da escala Clance. Quando a pontuação está entre 61 e 80, a pessoa tem sentimentos frequentes da síndrome, quando é maior que 80, os sentimentos além de frequentes são intensos. Sendo assim, quando ipScore é maior que 61, considera-se, neste trabalho, que existe a presença de Síndrome do Impostor.
Na pasta [testes](testes/), além do arquivo citado acima, existe um arquivo de teste do sistema, que demonstra que o script não funciona sem a coluna hasIP.


# Contato
Este script foi desenvolvido por Paloma Guenes. 
palomaguenes@gmail.com
