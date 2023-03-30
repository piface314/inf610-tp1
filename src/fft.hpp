// Implementation based on: https://gist.github.com/lukicdarkoo/3f0d056e9244784f8b4a

#ifndef FFT_H
#define FFT_H

#include <cmath>
#include <complex>
#include <vector>

typedef std::complex<double> Complex;

struct SignalDesc {
    double f, a, b;
};

void fft(double x_in[], Complex x_out[], int n, int &op);
void dft(double x_in[], Complex x_out[], int n);
void create_signal(int n, SignalDesc sd, std::vector<double>& signal);
void merge_signals(int n, std::vector<std::vector<double>>& signals, double result[]);

#endif