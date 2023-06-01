#include <iostream>
#include "shortest_path.hpp"

using namespace std;

int main() {
    GrafoCPP g(4);

    g.adicionaArco(0, 1, 2);
    g.adicionaArco(0, 2, 1);
    g.adicionaArco(1, 3, 3);
    g.adicionaArco(2, 3, 6);

    cout << "Grafo gerado:" << endl;
    cout << g;

    int *dist = g.caminhoMinimo(0, 3);
    cout << "Distância mínima entre 0 e 3: " << dist[3] << endl;

    return 0;
}
