import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from src.pricing import black_scholes
from src.greeks import calculate_greeks


def plot_call_price_vs_volatility():
    volatilities = np.linspace(0.05, 0.6, 100)
    call_prices = []

    S = 100
    K = 100
    T = 1
    r = 0.05

    for sigma in volatilities:
        call_price, _ = black_scholes(S, K, T, r, sigma)
        call_prices.append(call_price)

    output_dir = Path("figures")
    output_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(volatilities, call_prices, linewidth=2)
    plt.title("Call Option Price vs Volatility")
    plt.xlabel("Volatility (sigma)")
    plt.ylabel("Call Option Price")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "call_price_vs_volatility.png", dpi=300)
    plt.show()


def plot_greeks_vs_stock_price():
    stock_prices = np.linspace(50, 150, 200)

    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    call_deltas = []
    gammas = []
    vegas = []

    for S in stock_prices:
        call_delta, _, gamma, vega, _, _, _, _ = calculate_greeks(S, K, T, r, sigma)
        call_deltas.append(call_delta)
        gammas.append(gamma)
        vegas.append(vega)

    output_dir = Path("figures")
    output_dir.mkdir(exist_ok=True)

    fig, axes = plt.subplots(3, 1, figsize=(8, 12), sharex=True)

    axes[0].plot(stock_prices, call_deltas, linewidth=2)
    axes[0].set_title("Call Delta vs Stock Price")
    axes[0].set_ylabel("Delta")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(stock_prices, gammas, linewidth=2)
    axes[1].set_title("Gamma vs Stock Price")
    axes[1].set_ylabel("Gamma")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(stock_prices, vegas, linewidth=2)
    axes[2].set_title("Vega vs Stock Price")
    axes[2].set_xlabel("Stock Price (S)")
    axes[2].set_ylabel("Vega")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "greeks_vs_stock_price.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    plot_call_price_vs_volatility()
    plot_greeks_vs_stock_price()
