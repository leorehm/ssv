**Fundamental Frequency Estimation**

**Fourier Series**: Every periodic function $ g(t) $ with period $ T_0 $ can be represented by a series of sine and cosine functions, whose frequencies are integer multiples of the fundamental frequency $ f_0 = \frac{1}{T_0} $:

$$ 
g(t) = \frac{a_0}{2} + \sum_{h=1}^{\infty} \left( a_h \cos(2\pi h f_0 t) + b_h \sin(2\pi h f_0 t) \right) 
$$

Let $ x(n) $ denote a realization of a random process

- Autocorrelation function
  $$ \phi_{XX}(\lambda) = E(x(n)x^*(n + \lambda)) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u v p_{x(n),x^*(n+\lambda)}(u, v) \, du \, dv $$

- The signal is shifted against itself → measure of self-similarity

- Estimation for a quasi-stationary segment of length $ N $ for lag $ \lambda > 0 $
  $$ \hat{\phi}_{xx}(\lambda) = \frac{1}{N - |\lambda|} \sum_{n=0}^{N-|\lambda|-1} x(n)x^*(n + \lambda) $$

- The Fourier transform of the autocorrelation function is called power spectral density (PSD)
  $$ \Phi_X(f) = \sum_{\lambda=-\infty}^{\infty} \phi_{XX}(\lambda)e^{-j\Omega\lambda} $$

White Noise

- Described by a Power Spectral Density constant over frequency (white)

- Power Spectral Density:
  $$ \Phi_X (\Omega) = \sigma^2_X $$

- Auto-Correlation function:
  $$ \phi_{XX}(\lambda) = \sigma^2_X \delta(\lambda) = \begin{cases} 
  \sigma^2_X & \lambda = 0 \\
  0 & \lambda \neq 0 
  \end{cases} $$

“White noise” implies that successive samples are uncorrelated.


**Spectral Analysis of Audio Signals**

Periodic signal → sum of harmonics

$$ 
x(t) = \frac{a_0}{2} + \sum_{h=1}^{\infty} \left( a_h \cos(2\pi h f_0 t) + b_h \sin(2\pi h f_0 t) \right) 
$$

The coefficients $a_h$, $b_h$ are obtained by computing the “similarity” between the signal and a sine/cosine as

$$
a_h = \frac{2}{T_0} \int_{0}^{T_0} x(t) \cos(2\pi h f_0 t) \, dt
$$

$$
b_h = \frac{2}{T_0} \int_{0}^{T_0} x(t) \sin(2\pi h f_0 t) \, dt
$$

Continuous-time Fourier transform

$$
X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t} \, dt
$$

$$
x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega)e^{j\omega t} \, d\omega
$$

where $X(j\omega)$ is a continuous and non-periodic function of $\omega = 2\pi f$.


**Vocal Tract Model and Linear Prediction**

**Sampling, Quantization and Speech Coding**

**Cepstral Analysis**

**Speech Enhancement**
