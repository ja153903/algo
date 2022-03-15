from ...src.google.lp2034 import StockPrice


def test_lp2034_flow():
    stock = StockPrice()
    stock.update(1, 10)
    stock.update(2, 5)

    assert stock.current() == 5
    assert stock.maximum() == 10
    
    stock.update(1, 3)

    assert stock.maximum() == 5
    
    stock.update(4, 2)
    
    assert stock.minimum() == 2
