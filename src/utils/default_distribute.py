import random


def default_distribute(cards, players, dealer, dog_size, set):
    distribution = []
    number_of_card_by_player = int((len(cards) - dog_size) / len(players))
    for player in players:
        [distribution.append(player) for _ in range(number_of_card_by_player)]
    [distribution.append(None) for _ in range(dog_size)]

    random.shuffle(distribution)
    return distribution
