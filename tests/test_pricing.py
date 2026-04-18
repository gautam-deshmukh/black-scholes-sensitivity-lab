from src.pricing import black_scholes


def test_black_scholes_at_the_money():
    call_price, put_price = black_scholes(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2
    )

    assert round(call_price, 2) == 10.45
    assert round(put_price, 2) == 5.57
