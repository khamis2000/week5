import random

def pick_one_name(names):
    """Pick one name at random from a list of names."""
    return random.choice(names)

def pick_n_names(names, n):
    """Pick n names from a list, returning them in the order they were selected."""
    return random.sample(names, k=n)
class Raffle:
    def __init__(self, max_people, max_tickets, ticket_price):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.ticket_price = ticket_price
        self.total_earnings = 0
        self.participants = {}  # Maps participant name to the number of tickets they hold

    def add_person(self, name):
        """Add a new person to the raffle with 0 tickets, if there's space."""
        if name not in self.participants and len(self.participants) < self.max_people:
            self.participants[name] = 0

    def buy_ticket(self, name, num_tickets=1):
        """A person can buy tickets, adding to the total earnings if tickets are available."""
        if name in self.participants:
            available_tickets = self.max_tickets - sum(self.participants.values())
            if available_tickets >= num_tickets:
                self.participants[name] += num_tickets
                self.total_earnings += num_tickets * self.ticket_price

    def select_winner(self):
        """Select one person to win the raffle, considering the number of tickets each bought."""
        total_tickets = sum(self.participants.values())
        if total_tickets == 0:
            return None
        winning_ticket = random.randint(1, total_tickets)
        current = 0
        for name, tickets in self.participants.items():
            current += tickets
            if current >= winning_ticket:
                return name
