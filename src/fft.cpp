#include "fft.hpp"

// Recursive FFT
void fft_rec(Complex x[], int n, int& op) {
  if (n <= 1)
    return;

  Complex x_e[n/2], x_o[n/2];
  for (int i = 0; i < n/2; ++i)
    x_e[i] = x[i*2], x_o[i] = x[i*2 + 1];
  fft_rec(x_e, n/2, op);
  fft_rec(x_o, n/2, op);

  for (int k = 0; k < n / 2; ++k) {
    ++op;
    Complex w = exp(Complex(0, -2*M_PI*k / n));
    x[k] = x_e[k] + x_o[k] * w;
    x[n/2 + k] = x_e[k] - x_o[k] * w;
  }
}

// Initial call to FFT
void fft(double x_in[], Complex x_out[], int n, int& op) {
  for (int i = 0; i < n; ++i)
    x_out[i] = Complex(x_in[i], 0);
  op = 0;
  fft_rec(x_out, n, op);
}

// Simple DFT, for reference
void dft(double x_in[], Complex x_out[], int n) {
  for (int k = 0; k < n; ++k) {
    x_out[k] = Complex(0.0, 0.0);
    for (int i = 0; i < n; ++i)
      x_out[k] += x_in[i] * exp(Complex(0, -2 * M_PI * k * i / n));
  }
}


// Creates a sample signal
void create_signal(int n, SignalDesc sd, std::vector<double>& signal) {
  for (int i = 0; i < n; ++i)
    signal.push_back(sd.a * sin((2 * M_PI * sd.f * i) / n + sd.b));
}

// Combines multiple signals into one
void merge_signals(int n, std::vector<std::vector<double>>& signals, double result[]) {
  for (int i = 0; i < n; ++i) {
    result[i] = 0.0;
    for (auto signal : signals)
      result[i] += signal[i];
  }
}