import sys
from Genetic_Algorithm import Genetic_Algorithm

# main.py <tamanho-da-população> <numero-de-geraçãoes> <taxa-de-mutação> <taxa-de-crossover> <imprime-cada-geracao(1-true,2-false)>
def main():
    ga = None
    imprime_cada_geracao = None
    if len(sys.argv) != 6:
        print("Esperava-se o seguinte comando: \"python main.py <tamanho-da-população> <numero-de-geraçãoes> <taxa-de-mutação> <taxa-de-crossover> <imprime-cada-geracao>\"")
        print('Nao foi passado argumentos na linha de comando, o algoritmo será executado com as configuraçoes padrão')
        print('Tamanho da populacao: 30, Numero de Geraçoes: 20, Taxa de mutação: 1%, Taxa de crossover: 60%')
        ga = Genetic_Algorithm(-10, 10, 30, 20, 1, 60)
        imprime_cada_geracao = False
    else:
        print('O algoritmo genético funcionara com os seguintes parametros')
        print('Tamanho da populacao:', sys.argv[1], 'Numero de Geraçoes:', sys.argv[2], ', Taxa de mutação:', sys.argv[3], '%, Taxa de crossover:', sys.argv[4], '%')
        ga = Genetic_Algorithm(-10, 10, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        imprime_cada_geracao = True if int(sys.argv[5]) else False
    
    for i in range(ga.num_geracoes):
        # Calcula a aptidao da populacao atual
        ga.calcularAptidao()

        nova_populacao =[]

        while(len(nova_populacao) < ga.tam_populacao):
            
            # Seleciona os dois individuos pelo metodo da roleta
            pai = ga.selecao()
            mae = ga.selecao()

            # Crossover dos dois gerando os dois novos filhos
            filho_1, filho_2 = ga.crossover(pai, mae)

            # Fazendo a mutaca dos dois filhos
            filho_1 = ga.mutacao(filho_1)
            filho_2 = ga.mutacao(filho_2)

            nova_populacao.append(filho_1)
            nova_populacao.append(filho_2)
            # ga.renovarPopulacao(filho_1, filho_2)
        
        if imprime_cada_geracao:
            ga.imprimeComCusto(i)
        ga.populacao = nova_populacao


if __name__ == "__main__":
    main()