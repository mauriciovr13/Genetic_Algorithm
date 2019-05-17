from random import randint
from string import maketrans

class Genetic_Algorithm():
    """
        Algoritmo genético para encontrar o x para o qual a função x^2 - 3x + 4 assume o valor máximo
    """
    def __init__(self, x_min, x_max, tam_populacao, taxa_mutacao, taxa_crossover, num_geracoes):
    # Inicializa todos os atributos da instância
        self.x_min = x_min
        self.x_max = x_max
        self.tam_populacao = tam_populacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.num_geracoes = num_geracoes

        # calcula o número de bits do x_min e x_máx no formato binário com sinal
        qtd_bits_x_min = len(bin(x_min).replace('0b', '' if x_min < 0 else '+'))
        qtd_bits_x_max = len(bin(x_max).replace('0b', '' if x_max < 0 else '+'))

        # o maior número de bits representa o número de bits a ser utilizado para gerar individuos
        self.num_bits = qtd_bits_x_max if qtd_bits_x_max >= qtd_bits_x_min else qtd_bits_x_min

        # gera os individuos da população
        self._gerarPopulacao()
        self.mostrarPopulacao()
    
    def _gerarPopulacao(self):
        # criando a lista de lista que será a populacao
        self.populacao = [[] for i in range(self.tam_populacao)]
        # preenchendo a população
        for individuo in self.populacao:
            # para cada individuo da populacao, sortei um numero entre x_min e x_max
            num =  randint(self.x_min, self.x_max)
            # convertendo o num para um formato binario com sinal
            # zfill preenche o numero para que todos os numeros gerados tenham o mesmo numero de bits
            # o num_bin usara o primeiro bit para ser o bit de sinal e o restante o bit do numero
            num_bin = bin(num).replace('0b', '' if num < 0 else '+').zfill(self.num_bits)
            # transfoma num_bin em um vetor para adicionar a populacao
            for bit in num_bin:
                individuo.append(bit)

    def mostrarPopulacao(self):
        for individuo in self.populacao:
            print(individuo)
        
    def calculaAptidao(self, num_bin):
        # Calcula a nota associada a cada indíviduo que avalia quão boa é a solução por ele representada.
        # Calcula a função objetivo utilizada para avlaiar as soluções produzidas

        # converte o número binário para o formato inteiro
        num = int(''.join(num_bin), 2)
        # calcula e retorna o resultado da função objetivo
        return num**2 - 3*num + 4
 
    def crossover(self, pai, mae):
        # Aplica o crossover de acordo com uma dada probabilidade (taxa de crossover)
        
        # Verifica a possibilidade de fazer crossover
        if randint(1, 100) <= self.taxa_crossover:
            # Escolher ponto de corte
            ponto_corte = randint(1, self.num_bits)
            filho_1 = pai[:]
            filho_1[:ponto_corte] = mae[ponto_corte:]
            filho_2 = mae[:]
            filho_2[:ponto_corte] = pai[ponto_corte:]
        else:
            filho_1 = pai[:]
            filho_2 = mae[:]
        
        return filho_1, filho_2

    def mutacao(self, individuo):
        # Realiza a mutação dos bits de um indiviuo conforme uma dada probabilidade (taxa de mutação)
        
        # Verificar a possibilidade de fazer mutacao
        if randint(1,100) <= self.taxa_mutacao:
            pos_mutacao = randint(0, self.num_bits)
            traducao = maketrans('+-10', '-+01')
            individuo = individuo.translate(traducao)
        
        return individuo
        
    def selecao(self):
        




