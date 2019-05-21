from random import randint, uniform

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
        print("Populacao inicial:")
        for individuo in self.populacao:
            print(individuo)
    
    def funcao_objetivo(self, num_bin):
        # Converte o número binário para o formato inteiro
        num = int(''.join(num_bin), 2)
        # Calcula e retorna o resultado da função objetivo
        return num**2 -3*num + 4

    def calcularAptidao(self):
        # Calcula a nota associada a cada indíviduo que avalia quão boa é a solução por ele representada.

        self.aptidao = []
        for individuo in self.populacao:
            self.aptidao.append(self.funcao_objetivo(individuo))
 
    def crossover(self, pai, mae):
        # Aplica o crossover de acordo com uma dada probabilidade (taxa de crossover)
        
        # Verifica a possibilidade de fazer crossover
        if randint(1, 100) <= self.taxa_crossover:
            # Escolher ponto de corte
            ponto_corte = randint(1, self.num_bits)
            # Fazer o corte
            filho_1 = pai[:ponto_corte] + mae[ponto_corte:]
            filho_2 = mae[:ponto_corte] + pai[ponto_corte:]

            self._ajustar(filho_1)
            self._ajustar(filho_2)
        else:
            # Caso contrário, os filhos serão copias exatas dos pais
            filho_1 = pai[:]
            filho_2 = mae[:]
        
        return filho_1, filho_2

    def mutacao(self, individuo):
        # Realiza a mutação dos bits de um indiviuo conforme uma dada probabilidade (taxa de mutação)
        
        # Verificar a possibilidade de fazer mutacao
        if randint(1,100) <= self.taxa_mutacao:
            # Escolher uma posicao aleatoria
            pos_mutacao = randint(0, self.num_bits-1)
            # Criar uma matriz de traducacao
            traducao = str.maketrans('+-10', '-+01')
            # Modificando a posicao escolhida
            individuo[pos_mutacao] = individuo[pos_mutacao].translate(traducao)

            self._ajustar(individuo)

        return individuo
        
    def selecao(self):
        # Essa função usa o metodo de roleta para selecionar os individuos

        # Calcula a propabilidade de selecao
        somaTotal = sum(self.aptidao)
        # Probabilidade de selecao dos individuso
        self.prob_selecao = []
        for i in range(len(self.aptidao)):            
            self.prob_selecao.append((self.aptidao[i]/somaTotal)*100)

        '''
            Inicio
                T = soma dos valores de aptidão de todos os indivíduos da população
                Repita N vezes para selecionar n indivíduos
                    r = valor aleatório entre 0 e T
                    Percorra sequencialmente os indivíduos da população, acumulando
                    em S o valor de aptidão dos indivíduos já percorridos
                    Se S >= r então
                        Selecione o indivíduo corrente
                    Fim se
                Fim Repita
            Fim
        '''
        # Soma dos valores de aptidao de todos os individuos da populacao
        soma = somaTotal
        selecionados = []
        # Guarda a aptidao ate o momento
        s = 0
        while(len(selecionados) < 2):
            # Seleciona um ponto flutuante aleatorio dentro do interavalo
            r = uniform(0, soma)
            for i in range(len(self.prob_selecao)):
                s += self.prob_selecao[i]
                if s >= r:
                    selecionados.append(self.populacao[i])
                    break
        # Retorna uma lista de selecionados com dois individuos                    
        return selecionados

    def _ajustar(self, individuo):
        # Função serve para ajustar os individos apos o crossover e a mutação
        # Pode ser que apos os operadores o valor saia dos limites

        # Converte o individuo em um numero inteiro
        numero = int(''.join(individuo), 2)
        if numero < self.x_min:
            # se o numero for menor que o limite minino, ele agora recebe o valor do limite minino
            limite = bin(self.x_min).replace('0b', '' if self.x_min < 0 else '+').zfill(self.num_bits)
            for indice, bit in enumerate(limite):
                individuo[indice] = bit

        elif numero > self.x_max:
            limite = bin(self.x_max).replace('0b', '' if self.x_max < 0 else '+').zfill(self.num_bits)
            for indice, bit in enumerate(limite):
                individuo[indice] = bit
    
    def renovarPopulacao(self, filho_1, filho_2):
        # Encontrar os indices do dois menores elementos da populacao
        menor_1 = 0
        for i in range(1, len(self.aptidao)):
            if(self.aptidao[i] < self.aptidao[menor_1]):
                menor_1 = i
        
        menor_2 = 0
        for j in range(1, len(self.aptidao)):
            if(self.aptidao[j] < self.aptidao[menor_2] and j != menor_1):
                menor_2 = i

        self.populacao[menor_1] = filho_1
        self.populacao[menor_2] = filho_2

    def imprimeComCusto(self, pop):
        print("Populacao", pop)
        for i in range(len(self.populacao)):
            print(self.populacao[i], self.aptidao[i], str(self.prob_selecao[i]) + "%")