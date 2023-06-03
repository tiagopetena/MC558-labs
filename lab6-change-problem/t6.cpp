#include <iostream>
#include <map>
#include "shortest_path.hpp"

using namespace std;


int main() {
    int nKinds = 0;
    int totalCost = 0;


    // Parse input
    scanf("%d %d", &nKinds, &totalCost);

    int* values = (int *) calloc(nKinds, sizeof(int *));
    int* weights = (int *) calloc(nKinds, sizeof(int *));
    int* quantities = (int *) calloc(nKinds, sizeof(int *));

    for (int i = 0; i < nKinds; i++)
    {
        scanf("%d %d %d", &values[i], &weights[i], &quantities[i]);    
    }


    // Count total number of coins
    int nCoins = 0;
    for (int i = 0; i < nKinds; i++)
    {
        nCoins += quantities[i];
    }
    cout << nCoins << endl;


    // Consider all coins unique
    int coinIdx = 0;
    int* allValues = (int *) calloc(nCoins, sizeof(int *));
    int* allWeights = (int *) calloc(nCoins, sizeof(int *));
    for (int i = 0; i < nKinds; i++)
    {
        for (int c = 0; c < quantities[i]; c++)
        {
            allValues[coinIdx] = values[i];
            allWeights[coinIdx] = weights[i];
            coinIdx++;
        }
    }

    // Create Graph
    int n_vertices = nCoins * (totalCost + 1) + 2;
    cout << "n_vertices: " << n_vertices << endl;
    int s = n_vertices - 1;
    int t = n_vertices - 2;
    GrafoCPP g(n_vertices);

    for (int c = nCoins - 1; c > 0; c--)
    {
        for (int l = 0; l <= totalCost; l++)
        {
            int vertexIdx = ((c * (totalCost + 1))) + l;

            g.adicionaArco(vertexIdx - (totalCost + 1), vertexIdx, 0);

            if (l - allValues[c] >= 0)
            {
                g.adicionaArco(vertexIdx - (totalCost + 1) - allValues[c], vertexIdx, allWeights[c]);
            }
        }
    }

    g.adicionaArco(s, 0, 0);
    g.adicionaArco(s, allValues[0], allWeights[0]);
    g.adicionaArco((nCoins) * (totalCost + 1) - 1, t, 0);

    cout << "Grafo gerado:" << endl;
    // cout << g;

    int *dist = g.caminhoMinimo(s, t);
    cout << "Distância mínima entre " << s << " e " << t << " " << dist[t] << endl;

    return 0;
}
