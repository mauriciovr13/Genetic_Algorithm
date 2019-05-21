import sys
from Genetic_Algorithm import Genetic_Algorithm

# main.py <tamanho-da-população> <numero-de-geraçãoes> <taxa-de-mutação> <taxa-de-crossover>
def main():
    ga = None
    if len(sys.argv) != 5:
        print("Esperava-se o seguinte comando: \"python main.py <tamanho-da-população> <numero-de-geraçãoes> <taxa-de-mutação> <taxa-de-crossover>\"")
        print('Nao foi passado argumentos na linha de comando, o algoritmo será executado com as configuraçoes padrão')
        print('Tamanho da populacao: 4, Numero de Geraçoes: 5, Taxa de mutação: 1%, Taxa de crossover: 60%')
        ga = Genetic_Algorithm(-10, 10, 4, 1, 60, 5)
    else:
        print('O algoritmo genético funcionara com os seguintes parametros')
        print('Tamanho da populacao:', sys.argv[1], 'Numero de Geraçoes:', sys.argv[2], ', Taxa de mutação:', sys.argv[3], '%, Taxa de crossover:', sys.argv[4], '%')
        ga = Genetic_Algorithm(-10, 10, int(sys.argv[1]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[2]))

    numGeracao = 0
    while(numGeracao < ga.num_geracoes):
        # Calcula a aptidao da populacao atual
        ga.calcularAptidao()

        # Seleciona os dois individuos pelo metodo da roleta
        pai, mae = ga.selecao()

        # Crossover dos dois gerando os dois novos filhos
        filho_1, filho_2 = ga.crossover(pai, mae)

        # Fazendo a mutaca dos dois filhos
        filho_1 = ga.mutacao(filho_1)
        filho_2 = ga.mutacao(filho_2)

        ga.renovarPopulacao(filho_1, filho_2)

        ga.imprimeComCusto(numGeracao)
        numGeracao += 1





if __name__ == "__main__":
    main()