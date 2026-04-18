import numpy as np
from scipy.stats import norm


def calculate_greeks(S, K, T, r, sigma):
    """
    Calculate Black-Scholes Greeks for European options.

    Returns
    -------
    tuple[float, float, float, float, float, float, float, float]
        call_delta, put_delta, gamma, vega, call_theta, put_theta, call_rho, put_rho
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    n_prime_d1 = norm.pdf(d1)

    gamma = n_prime_d1 / (S * sigma * np.sqrt(T))
    vega = S * np.sqrt(T) * n_prime_d1 / 100

    call_delta = norm.cdf(d1)
    put_delta = call_delta - 1

    call_theta = (
        -(S * n_prime_d1 * sigma) / (2 * np.sqrt(T))
        - r * K * np.exp(-r * T) * norm.cdf(d2)
    ) / 365

    put_theta = (
        -(S * n_prime_d1 * sigma) / (2 * np.sqrt(T))
        + r * K * np.exp(-r * T) * norm.cdf(-d2)
    ) / 365

    call_rho = (K * T * np.exp(-r * T) * norm.cdf(d2)) / 100
    put_rho = (-K * T * np.exp(-r * T) * norm.cdf(-d2)) / 100

    return call_delta, put_delta, gamma, vega, call_theta, put_theta, call_rho, put_rho
