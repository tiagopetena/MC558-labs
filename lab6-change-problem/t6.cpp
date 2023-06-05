#include <iostream>
#include "shortest_path.hpp"

using namespace std;

int main()
{
    int nKinds = 0;
    int totalCost = 0;

    // Parse input
    scanf("%d %d", &nKinds, &totalCost);

    int *values = (int *)malloc(nKinds * sizeof(int *));
    int *weights = (int *)malloc(nKinds * sizeof(int *));
    int *quantities = (int *)malloc(nKinds * sizeof(int *));

    for (int i = 0; i < nKinds; i++)
    {
        scanf("%d %d %d", &values[i], &weights[i], &quantities[i]);
    }

    // Create Graph
    int n_vertices = nKinds * (totalCost + 1) + 2;
    int s = n_vertices - 1;
    int t = n_vertices - 2;
    Grafo g(n_vertices);

    for (int c = nKinds - 1; c > 0; c--)
    {
        for (int l = 0; l <= totalCost; l++)
        {
            int vertexIdx = ((c * (totalCost + 1))) + l;

            g.adicionaArco(vertexIdx - (totalCost + 1), vertexIdx, 0);
            for (int q = 1; q <= quantities[c]; q++)
            {
                if (l - (q*values[c]) >= 0)
                {
                    g.adicionaArco(vertexIdx - (totalCost + 1) - (q*values[c]), vertexIdx, q*weights[c]);
                }
                else
                {
                    break;
                }
            }
        }
    }

    g.adicionaArco(s, 0, 0);
    for (int q = 1; q <= quantities[0]; q++)
        {
            if (q*values[0] >= 0)
            {
                g.adicionaArco(s, q*values[0], q*weights[0]);
            }
        }
    int targetCostNode = (nKinds) * (totalCost + 1) - 1;
    g.adicionaArco(targetCostNode, t, 0);

    int *dist = g.caminhoMinimo(s, t);
    if (dist[t] < INT_MAX)
    {
        cout << dist[t] << endl;
    }
    else
    {

        for (int l = 1; l <= totalCost; l++)
        {
            int resultCost = targetCostNode - l;
            if (dist[resultCost] < INT_MAX)
            {
                cout << (totalCost - l) << " " << dist[resultCost] << endl;
                break;
            }
        }
    }

    // free(values);
    // free(weights);
    // free(quantities);

    return 0;
}
