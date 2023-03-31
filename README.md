# INF610 - Trabalho Prático 1

Trabalho Prático 1 da disciplina INF610 - Estruturas de Dados e Algoritmos, no programa de mestrado em Ciência da Computação pela Universidade Federal de Viçosa.

## Compilação

Tendo o `make` e o `g++` instalado, basta executar o comando `make`.

## Uso

Ao chamar o executável, especifique o algoritmo a ser executado, `dijkstra` ou `fft`.
Em seguida, é possível especificar um arquivo de entrada e um arquivo de saída.
Caso sejam omitidos, a entrada e a saída padrão serão usadas.

```bash
$ ./bin/inf610-tp1 <algorithm> [<inpath> <outpath>]
```

### Dijkstra

A entrada deve ter o seguinte padrão:
- Uma linha inicial diz o tamanho do próximo caso de teste, contendo o número de vértices, de arestas e a o vértice inicial, separados por espaço;
- Depois dessa linha se segue uma linha para cada aresta, sendo cada aresta representada por um par de vértices e um peso.
- Pode haver qualquer quantidade de casos de teste.

Veja `data/dijkstra-example.txt` e `data/dijkstra-test-case.txt` como exemplos.

### FFT

A entrada deve ter o seguinte padrão: cada linha é um caso de teste, contendo, em ordem:
- o tamanho da entrada, ou seja, a quantidade de amostras no sinal;
- a quantidade de sinais a serem combinados antes de passar para a transformada;
- a descrição de cada sinal, que são grupos e 3 números, indicando frequência, amplitude e fase da onda.

Veja `data/fft-example.txt` e `data/fft-test-case.txt` como exemplos.
