from src.pricing import black_scholes
from src.greeks import calculate_greeks
from src.utils import get_float_input


def main():
    print("Black-Scholes Sensitivity Lab")
    print("-" * 32)

    spot_price = get_float_input("Enter the spot price (S): ")
    strike_price = get_float_input("Enter the strike price (K): ")
    time_to_expiration = get_float_input("Enter the time to expiration in years (T): ")
    risk_free_rate = get_float_input(
        "Enter the risk-free interest rate (r) as a decimal (e.g., 0.05 for 5%): "
    )
    volatility = get_float_input(
        "Enter the volatility (sigma) as a decimal (e.g., 0.2 for 20%): "
    )

    call_option_price, put_option_price = black_scholes(
        spot_price,
        strike_price,
        time_to_expiration,
        risk_free_rate,
        volatility,
    )

    (
        call_delta,
        put_delta,
        gamma,
        vega,
        call_theta,
        put_theta,
        call_rho,
        put_rho,
    ) = calculate_greeks(
        spot_price,
        strike_price,
        time_to_expiration,
        risk_free_rate,
        volatility,
    )

    print("\n--- Option Prices ---")
    print(f"Call Option Price: {call_option_price:.2f}")
    print(f"Put Option Price: {put_option_price:.2f}")

    print("\n--- The Greeks ---")
    print(f"Call Delta: {call_delta:.4f}")
    print(f"Put Delta: {put_delta:.4f}")
    print(f"Gamma: {gamma:.4f}")
    print(f"Vega: {vega:.4f}")
    print(f"Call Theta (per day): {call_theta:.4f}")
    print(f"Put Theta (per day): {put_theta:.4f}")
    print(f"Call Rho: {call_rho:.4f}")
    print(f"Put Rho: {put_rho:.4f}")


if __name__ == "__main__":
    main()
