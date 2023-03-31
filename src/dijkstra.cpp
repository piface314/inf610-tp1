#include "dijkstra.hpp"

int **create_adj(int n) {
  int *v = (int *)malloc(sizeof(int) * n * n);
  if (v == NULL)
    exit(1);
  for (int i = 0; i < n*n; ++i)
    v[i] = -1;
  int **adj = (int **)malloc(sizeof(int *) * n);
  for (int i = 0; i < n; ++i)
    adj[i] = v + i*n;
  return adj;
}

void dijkstra(int **adj, int n, int v_o,
              int d[], int p[], int &op) {
  int vt[n] = {0};
  for (int i = 0; i < n; ++i)
    d[i] = INF, p[i] = -1;
  d[v_o] = 0, p[v_o] = v_o;

  for (int c = 0; c < n-1; ++c) {
    int u = -1;
    for (int i = 0; i < n; ++i)
      if (++op && !vt[i] && (u==-1 || d[i] < d[u]))
        u = i;
    for (int v = 0; v < n; ++v) {
      int w = adj[u][v];
      if (++op && w >= 0 && d[u] + w < d[v])
        d[v] = d[u] + w, p[v] = u;
    }
    vt[u] = 1;
  }
}
