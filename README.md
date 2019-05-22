# Algoritmo Genético

## Exercício da disciplina de Inteligência Artificial - UFLA - 2019/1:

Algoritmo genético para encontrar o valor de x para o qual a função f(x) = x² - 3x + 4 assume o valor máximo.

- Assumir que x [-10, +10];
- Codificar x como vetor binário;

## Modo de Execução
Digite o comando abaixo no terminal

`python main.py <tamanho-da-população> <numero-de-gerações> <taxa-de-mutação> <taxa-de-crossover> <imprimir-cada-geracao(1-true,2-false)>`

Se não for passado os argumentos necessários, o programa executará com os seguintes parametros:
- População com 30 indivíduos
- Usará 20 gerações
- Taxa de mutação de 1%
- Taxa de crossover de 60%
- Não mostrará a população depois de cada geração
