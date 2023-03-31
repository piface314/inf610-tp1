#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#define INF std::numeric_limits<int>::max()

#include <limits>
#include <cstdlib>

int **create_adj(int n);
void dijkstra(int **adj, int n, int v_o, int dist[], int prev[], int &op);

#endif