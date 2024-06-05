# Turing Machines

This is a simple implementation of a Turing Machine in Python. It is based on the definition of a Turing Machine as a 5-tuple (Q, Σ, Γ, q0, δ), where:
- Q is a finite set of states, assumed not to contain h, the halt state
- Σ, the input alphabet, is a finite set of symbols
- Γ, the tape alphabet, is a finite set with Σ ⊆ Γ; Γ is assumed not to contain Δ, the blank symbol
- q0 ∈ Q is the initial state
- δ is a partial function (i.e. possibly undefined at some points):

    δ: Q × (Γ ∪ {Δ}) → (Q ∪ {h}) × (Γ ∪ {Δ}) × {L, R, S}

The machine is run by providing an initial tape, and the machine will run until it halts. The machine will halt if it reaches the halt state.


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