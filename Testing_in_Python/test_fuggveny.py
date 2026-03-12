import fuggveny
from unittest.mock import MagicMock

def test_mai_ev(monkeypatch):
    mock_dt = MagicMock()
    mock_dt.today.return_value.year = 2020
    monkeypatch.setattr(fuggveny, "datetime", mock_dt)

    assert fuggveny.mai_ev() == 2020