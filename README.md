# Turing Machines

This is a simple implementation of a Turing Machine in Python. It is based on the definition of a Turing Machine as a 5-tuple (Q, Σ, Γ, q0, δ), where:
- Q is a finite set of states, assumed not to contain h, the halt state
- Σ, the input alphabet, is a finite set of symbols
- Γ, the tape alphabet, is a finite set with Σ ⊆ Γ; Γ is assumed not to contain Δ, the blank tape symbol
- q<sub>0</sub> ∈ Q is the initial state
- δ is a partial function (i.e. possibly undefined at some points):

    δ: Q × (Γ ∪ {Δ}) → (Q ∪ {h}) × (Γ ∪ {Δ}) × {L, R, S}

The Turing Machine M accepts x ∈ Σ* if starting M with input x leads to a halting configuration.
In other words, x is accepted if for some strings y and z in (Γ ∪ {Δ})* and for some a ∈ Γ ∪ {Δ}:
(q<sub>0</sub>, <u>Δ</u>x) ⊢*<sub>M</sub> (h, y<u>a</u>z)

We say M halts on input x and L(M), the language accepted by M, is the set of input strings accepted by M: L(M) = { x ∈ Σ* | (q<sub>0</sub>, <u>Δ</u>x) ⊢*<sub>M</sub> (h, y<u>a</u>z) }.

## Machines

- `x_squared`: this machine will square the input number. The input number should be in unary, i.e. a sequence of 1s. The machine will replace the input with a sequence of 1s equal to the square of the input. For example, if the input is `111`, the machine will replace it with `111111111`.


## Requirements

- `pygame 2.5.2`

```bash
pip install requirements.txt
```


## Usage

```bash
python main.py
```

## Demo

![](resources/x_squared.gif)
*function: `f(x) = x²`*  
*input: `11111`*  
*output: `1111111111111111111111111`*

---

**Authors:** [Elia Innocenti](https://github.com/eliainnocenti), [Antonio Natale Bruno](https://github.com/antnatb)

**Contacts:** [elia.innocenti@edu.unifi.it](mailto:elia.innocenti@edu.unifi.it), [antonio.bruno@edu.unifi.it](mailto:antonio.bruno@edu.unifi.it)