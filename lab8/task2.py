import random

def generate_lottery_ticket():
    ticket = random.sample(range(1, 50), 6)
    return ticket

lottery_ticket = generate_lottery_ticket()

print(f"Ваш лотерейный билет: {lottery_ticket}")