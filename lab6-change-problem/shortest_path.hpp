#ifndef PATH_HPP
#define PATH_HPP

extern "C" {
#include "shortest_path.h"
}

using namespace std;

class GrafoCPP {

    Grafo *grafo;

    /* para facilitar seu debug */
    friend ostream &operator<<(ostream &output, const GrafoCPP &p);

public:
    /* cria um novo grafo vazio */
    GrafoCPP();

    /* cria um novo grafo com n vértices */
    GrafoCPP(int n);

    /* retorna o número de nós do grafo */
    int size();

    /* adiciona um vértice ao grafo
     * devolve o índice do novo vértice */
    int adicionaVertice();

    /* adiciona um arco de u a v com peso w
     * 0 <= u, v <= n-1  */
    void adicionaArco(int u, int v, int w);

    /* número de arcos do grafo */
    int numArcos();

    /* calcula um caminho mínimo de s a t num grafo sem ciclos orientados
     * devolve o custo de um caminho mínimo */
    int *caminhoMinimo(int s, int t);
};

#endif // PATH_HPP
