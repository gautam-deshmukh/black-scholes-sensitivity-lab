# Black-Scholes Sensitivity Lab

A Python project for pricing European call and put options with the Black-Scholes model and analyzing parameter sensitivity through the Greeks.

## Project background

This project originally began as a single Python file that implemented Black-Scholes option pricing and basic sensitivity analysis. I later refactored it into a structured GitHub repository to improve code organization, readability, reproducibility, and future extensibility.

## Features

- Black-Scholes pricing for European call and put options
- Greeks-based sensitivity analysis
- Modular Python code structure
- Room for plots, experiments, and tests
- Refactored from a single-file script into a cleaner project layout

## Repository structure

```text
black-scholes-sensitivity-lab/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── main.py
├── src/
│   ├── __init__.py
│   ├── pricing.py
│   ├── greeks.py
│   └── utils.py
├── notebooks/
├── tests/
└── figures/
```

## Tech stack

- Python
- NumPy
- SciPy
- Matplotlib

## Getting started

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/black-scholes-sensitivity-lab.git
cd black-scholes-sensitivity-lab
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Current status

The repository scaffold has been created and the original single-file implementation is being refactored into modular components.

## Planned improvements

- Add clean pricing and Greeks modules
- Add visualizations for sensitivity analysis
- Add unit tests for known option-pricing cases
- Add a notebook for exploration and demonstrations
- Potentially extend the project with implied volatility or Monte Carlo pricing

## Author

Gautam Deshmukh
