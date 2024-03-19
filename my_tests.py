import pytest
from my_functions import pick_one_name, pick_n_names, Raffle  

def test_pick_one_name():
    names = ["Alice", "Bob", "Charlie"]
    assert pick_one_name(names) in names

def test_pick_n_names():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    picked_names = pick_n_names(names, 2)
    assert len(picked_names) == 2
    for name in picked_names:
        assert name in names

@pytest.fixture
def sample_raffle():
    return Raffle(max_people=5, max_tickets=100, ticket_price=10)

def test_add_person(sample_raffle):
    sample_raffle.add_person("Eve")
    assert "Eve" in sample_raffle.participants
    assert sample_raffle.participants["Eve"] == 0

def test_buy_ticket(sample_raffle):
    sample_raffle.add_person("Eve")
    sample_raffle.buy_ticket("Eve", 5)
    assert sample_raffle.participants["Eve"] == 5
    assert sample_raffle.total_earnings == 50

def test_select_winner(sample_raffle):
    sample_raffle.add_person("Eve")
    sample_raffle.add_person("Adam")
    sample_raffle.buy_ticket("Eve", 1)
    sample_raffle.buy_ticket("Adam", 1)
    winner = sample_raffle.select_winner()
    assert winner in ["Eve", "Adam"]
