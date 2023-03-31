#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include "fft.hpp"
#include "dijkstra.hpp"

void run_test_case_dijkstra(std::istream &test_case, std::ostream &log);
void run_test_case_fft(std::istream &test_case, std::ostream &log);

int main(int argc, char const *argv[]) {
  if (argc < 2) {
    std::cerr << "Usage:\n  $ " << argv[0] << "<algorithm> <test-case-file> <log-output>\n";
    return 1;
  }
  std::string algorithm(argv[1]);
  
  std::ifstream test_case;
  std::ofstream log;
  std::istream *in = &std::cin;
  std::ostream *out = &std::cout;

  if (argc > 2) {
    test_case.open(argv[2]);
    if (!test_case.is_open()) {
        std::cerr << "No file `" << argv[2] << "`.\n";
        return 1;
    }
    in = &test_case;
  }

  if (argc > 3) {
    log.open(argv[3]);
    if (!log.is_open()) {
        std::cerr << "Error opening `" << argv[3] << "`.\n";
        return 1;
    }
    out = &log;
  }
  
  if (algorithm == "dijkstra")
    run_test_case_dijkstra(*in, *out);
  else if (algorithm == "fft")
    run_test_case_fft(*in, *out);
  else {
    std::cerr << "Unknown option `"<< algorithm << "` for algorithm.\n";
    return 1;
  }
  return 0;
}

void run_test_instance_dijkstra(std::ostream &log, int **adj, int n, int v_0) {
  int d[n], p[n], op = 0;
  dijkstra(adj, n, v_0, d, p, op);
  log << n << " " << v_0 << " " << op << "\n";
  log << "D: ";
  for (int i = 0; i < n; ++i)
    log << d[i] << " ";
  log << "\n";
  log << "P: ";
  for (int i = 0; i < n; ++i)
    log << p[i] << " ";
  log << "\n";
}

void run_test_case_dijkstra(std::istream &test_case, std::ostream &log) {
  int n, e, v_0, u, v, w;
  int **adj = NULL;
  while (test_case >> n >> e >> v_0) {
    adj = create_adj(n);
    for (int i = 0; i < e; ++i) {
      test_case >> u >> v >> w;
      adj[u][v] = w;
      adj[v][u] = w;
    }
    run_test_instance_dijkstra(log, adj, n, v_0);
  }  
}

void run_test_instance_fft(std::ostream &log, std::vector<SignalDesc> &sds, int n_samples) {
  size_t n_signals = sds.size();

  std::vector<std::vector<double>> signals;
  double signal[n_samples];

  for (size_t i = 0; i < n_signals; ++i) {
    signals.emplace_back();
    create_signal(n_samples, sds[i], signals[i]);
  }
  merge_signals(n_samples, signals, signal);

  Complex freq_domain[n_samples];
  int op = 0;
  fft(signal, freq_domain, n_samples, op);

  log << n_samples << " " << op << "\n";
  for (auto sd : sds)
    log << sd.f << " " << sd.a << " " << sd.b << " ";
  log << "\n";
  for (int i = 0; i < n_samples; ++i)
    log << "(" << std::fixed << std::setprecision(3) << freq_domain[i].real() << " " << freq_domain[i].imag() << ") ";
  log << "\n";
}

void run_test_case_fft(std::istream &test_case, std::ostream &log) {
  int n_samples, n_freqs;
  SignalDesc sd;
  std::vector<SignalDesc> sds;
  while (test_case >> n_samples >> n_freqs) {
    sds.clear();
    for (int i = 0; i < n_freqs; ++i) {
      test_case >> sd.f >> sd.a >> sd.b;
      sds.push_back(sd);
    }
    run_test_instance_fft(log, sds, n_samples);
  }
}

