import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from src.pricing import black_scholes


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
    output_path = output_dir / "call_price_vs_volatility.png"

    plt.figure(figsize=(8, 5))
    plt.plot(volatilities, call_prices, linewidth=2)
    plt.title("Call Option Price vs Volatility")
    plt.xlabel("Volatility (sigma)")
    plt.ylabel("Call Option Price")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()


if __name__ == "__main__":
    plot_call_price_vs_volatility()
