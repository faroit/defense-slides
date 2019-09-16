# General status

* [paperliste aktualisieren]
* [ ] source filter nmf is missing!

# Fragen an Antoine

* Chapter 2 is a mix between a literature overview and a fundamentals chapter
* Why doesn't shift-invariant NMF solve the vibrato case? or does it?

- source filter (vocals) + NMF (accompaniment) can solve vibrato but has a fixed dictionary for which parameters would need to be fitted. It works for all kind of modulations (e.g. guitar)
- common fate in comparison uses an FFT to get repetitions.

# Is deep learning a black box?

No, but From Chollet
> The same is true of backprop in deep learning -- knowing how to code up backprop by hand gives you no useful knowledge wrt deep learning, and inversely, developing powerful mental models for deep learning does not in any way require knowing the algorithmic details of backprop

# Defense

* color coded formular https://rockt.github.io/2018/04/30/einsum

##

* understanding cross entropy: https://rdipietro.github.io/friendly-intro-to-cross-entropy-loss/#cross-entropy

## Questions

- What is common fate (read paper)

## Modulation

! [] Elbow method, BIC, etc


- why does FM cause AM?

## Count Estimation

- explain how to count
- gap statistics, elbow, BIC

## time warping by applying non-linear resampling

- normally its x(n) := f[n*t], how does it work for invariant pitch
- introducing a `timeScaleFactor = 1.0/targetPitch` so that we get a constant pitch

## Wackelkandidaten

- * For the linear mixing case, the process can be transferred to the frequency domain as the Fourier transform is a linear operator.
% However, since we are normally dealing with the non-negative magnitude representation this is only an approximation~\cite{klapuri06book}.

### NMF, NTF

- explain the beta divergence
- how to derive the cost functions
- Erklärung von Antoine/Vincent
- understand HR-NMF, shift-invariant-nmf, hennquin10
- warum kein   auf CFT? Siehe pardo journal oder response

- READ: Towards music understanding without separation: Segmenting music with correlogram comodulation

### Separation

- Warum wiener filter für power spectrum?

### Backprop

- How does Guided Backpropagation work?
- http://blog.qure.ai/notes/deep-learning-visualization-gradient-based-methods

# Random s*** for my presentation

* [x] example that works quite nice... http://sisec17.audiolabs-erlangen.de/#/listen/20/STO1?mode=embed

# BEYOND EQUAL-LENGTH SNIPPETS: HOW LONG IS SUFFICIENT TO RECOGNIZE AN AUDIO SCENE? &* https://arxiv.org/pdf/1811.01095.pdf

### When to apply machine learning

Humans are unable to explain their expertise(e.g. Speech recognition, vision, language)
Solution changes with time(e.g. tracking, noise cancellation, adaptive filtering )
Solution needs to be adapted to particular cases(e.g. biometrics, personalization

* [ ] durchgehen: https://perso.telecom-paristech.fr/grichard/Enseignements/AIC/Bases-signal-pour-traitement-parole.pdf

### COUNT Distributions

you could go for non parametric (quantile regression) and aim for linimum confidence interval for instance

### Vibrato NTF by Creager

ok not activation then the vocabulary is=decision
because we output posterior distribution
1:36 PM
and decide afterwards

# Thesis Bib Notes

## Introduction

### [111] Haykin90

* Cherry invented the cocktail party problem
* Analysis and Synthesis are different problems to solve. A machine is rather concerned about synthesis
* Selective Attention (ignore other sources) vs. Divided attention (Simulultanous listening)
* Also: switched attention

### [32] Bregman90

Five principles of Auditory Scene Analysis

1. Proximity
2. Similarity
3. Continuity
4. Closure (completes fragmentures)
5. Common Fate (groups together activities (onset, glides, vibrato)
	AM and FM!

### Haykin DNN

* [ ] TODO: backpropagation p153

### [169] Antoine13

* [ ] TODO: explain Gaussian model and MWF
* [ ] TODO: What is PSD?

#### Problem with RNN 

* RNN computations are sequential
* 

### Eric Scheirer 

understanding without separation

