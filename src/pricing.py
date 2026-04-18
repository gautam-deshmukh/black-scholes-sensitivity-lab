import numpy as np
from scipy.stats import norm


def black_scholes(S, K, T, r, sigma):
    """
    Calculate Black-Scholes prices for European call and put options.

    Parameters
    ----------
    S : float
        Spot price of the underlying asset.
    K : float
        Strike price.
    T : float
        Time to expiration in years.
    r : float
        Risk-free interest rate as a decimal.
    sigma : float
        Volatility as a decimal.

    Returns
    -------
    tuple[float, float]
        Call price, put price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call_price, put_price

