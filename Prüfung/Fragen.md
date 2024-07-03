

# Questions

## Introduction

*What are the most important classes of speech sounds?*

voiced sounds
- vowels (a,e,i,o,u)
- sounds with mixed excitation (/v/)

unvoiced sounds
- fricative (/s/,/th/,/sh/)
- plosive (/k/,/p/,/t/)


*What is the difference between a phone and a phoneme? What is an allophone?*

- **Phone**: Smallest speech segment with distinct physical or perceptual properties.
  - **Example**: The sound [p] in the words "pat" and "spat" are two instances of the same phone.

- **Phoneme**: The smallest contrastive linguistic unit which may bring about a change of meaning. One phoneme consists of a set of phones that are thought of as the same element within the phonology of a particular language (→ allophones).
  - **Example**: The phoneme /p/ in English can change the meaning of a word, as in "pat" vs. "bat".

- **Allophone**: One phone of the many that constitute a phoneme.
  - **Example**: The [p] sound in "pat" (aspirated) and the [p] sound in "spat" (unaspirated) are allophones of the phoneme /p/ in English.

*How can phones be categorized into an international phonetic alphabet?*

Phonemes are characterized by the way of articulation
- Vowel
- Nasal
- Fricative
- Plosive


*What comprises prosody?*

Rhythm, stress, and intonation of speech
- Reflects
  - Emotional state of the speaker
  - Form of the utterance (statement, question, or command)
  - Irony or sarcasm
  - Emphasis, contrast, and focus

Remark: Often, only the intonation is meant when we say 'prosody'. However, intonation is strictly speaking only part of the prosody.


*How does human speech production work?*

- Lungs produce air flow
- In the larynx (Kehlkopf) the vocal cords start vibrating and produce sound
- In the vocal tract, the sound is formed to produce a speech sound.


*How can human speech production be modeled in a simplified framework?*

//Todo

*What is the difference between formant frequency and fundamental frequency*

*Note: Essential for passing this course*

*What is a formant map?*

*What are the three essential parts of the human ear?*

*Why is a spectral representation of audio signal so easy to interpret for humans?*

## Fundamental Frequency Estimation

*What is a typical range for the fundamental frequency of humans*

*What are average fundamental frequencies for female and male speakers, respectively?*

*How is it possible to distinguish female from male speakers in narrowband telephony?*

*How can the fundamental frequency of phones be measured?*

*How would you choose the segment/window length when estimating the varying fundamental frequency of speech? What is the trade-off?*

## Spectral Analysis of Audio Signals

*What are complex numbers and how can they be represented?*

*How are real and imaginary part related to magnitude and phase?*

*What is Euler's relation?*

*For what kind of signals would you use a Fourier series analysis, and for which a Fourier transform to analyze its spectral content?*

*Fourier transform pairs: What is the Fourier transform of an Impulse?*

*a rectangular function?*

*a sinusoid?*

*a delta comb?*

*a periodic signal like a sawtooth signal (qualitatively)?*

*What is a linear time-invariant (LTI) system? Give examples.*

*How can the relation between the input and the output of an LTI system be mathematically described in time and frequency domain, respectively?*

*How does a discretization of the time domain signal affect its spectrum?*

*How does a discretization of the spectrum of a signal affect its time-domain representation?*

*Explain the sampling theorem*

*What are typical sampling rates for speech and audio signals, respectively? Why?*

*What is cyclic convolution, and how can it be avoided?*

*What are the pros and cons for tapered spectral analysis windows, like a Hann windows, when compared to a rectangular window?*

*What is the difference between a wideband and a narrowband spectrogram wrt the visible properties of speech signals?*

*How is a time delay by one sample represented in the z-domain?*

## Vocal Tract Model and Linear Prediction

*Sketch and explain the source-filter model*

*How many Formants do we expect in speech signals per kHz? How many in a speech signal sampled at 16kHz?*

*How is the Kelly-Lochbaum structure related to the tube model of the vocal tract?*

*How is the Kelly-Lochbaum structure related to digital filtering?*

*What's the difference between the fundamental frequency and the formant frequency?*

*How can a system with an infinite impulse response be described with a finite amount of parameters?*

*What is a moving average system? How is it related to an all-zero system?*

*What is an autoregressive system? How is it related to an all-pole system?*

*What are linear predictive coefficients?*

*Why are they called "linear predictive"? What is predicted?*

*How are they derived?*

*How are LPC coefficients computed from a speech signal?*

*How many LPC coefficients do I need to model a speech signal? What does it depend on?*

*What is Pre-Emphasis? Why is it important?*

## Sampling, Quantization and Speech Coding

*What steps are necessary to digitize an analog signal?*

*Explain the sampling theorem graphically in the time and frequency domain*

*What is a Midrise Characteristic?*

*Why does the SNR suddenly drop if the signal power PS is large?*

*What is a companding scheme, and why is it used?*

*What is adaptive quantization?*

*What is vector quantization?*

*Name three fundamental speech coding schemes, along with their benefits and drawbacks*

*What coding scheme has been used in ISDN telephony and DECT telephony, and what are the datarates?*

## Cepstral Analysis

*In time domain, we have the signal model s(n)=h(n)∗e(n) with h(n) the impulse response of the vocal tract and e(n) the excitation signal. How does this signal model look in the cepstral domain*

*Is the complex cepstrum complex-valued?*

*How can we estimate the spectral envelope caused by the vocal tract from the cepstral representation?*

*How can we estimate the speech fundamental frequency in the cepstral domain?*

*Explain the meaning of the terms: Cepstrum, Quefrency, Liftering, Rahmonic*

## Speech Enhancement

*How is the Wiener Filter defined in the STFT domain?*

*Explain how the Wiener Filter works in the STFT?*

*Sketch the derivation of the Wiener Filter*

*How are posterior, likelihood and prior defined in Bayesian estimation?*

*How can I find a Bayesian MMSE estimator of clean speech?*

*Explain different methods to estimate the speech variances*

*Explain different methods to estimate the noise variances*

*What is the key advantage when multiple microphones are present?*

*Name and explain two different beamformers*

*What is the key advantage of an MVDR beamformer over a delay-and-sum beamformer?*
