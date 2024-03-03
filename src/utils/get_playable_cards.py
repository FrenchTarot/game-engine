from typing import List

from src.classes.Card import Card
from src.types.CardType import Trump
from src.types.CardValue import Fool


def get_playable_cards(owned_cards: List[Card], played_cards: List[Card]):
    not_played_cards = [card for card in owned_cards if not card.played]
    player_s_fool_card = [card for card in not_played_cards if card.value == Fool]

    owned_types = list(
        set([card.type for card in not_played_cards if card.value != Fool])
    )

    typing_card = [card for card in played_cards if card.value != Fool]
    if len(typing_card):
        asked_type = typing_card[0].type
        asked_rank = typing_card[0].value.rank

        if asked_type != Trump and asked_type in owned_types:
            # if this not a Trump and we own the asked type, we must play the must type or Fool
            return [
                card for card in not_played_cards if card.type == asked_type
            ] + player_s_fool_card
        elif asked_type == Trump and Trump in owned_types:
            greater_trump_card = [
                card
                for card in not_played_cards
                if card.value.rank > asked_rank and card.type == Trump
            ]
            lower_trump_card = [
                card
                for card in not_played_cards
                if card.value.rank < asked_rank and card.type == Trump
            ]

            if len(greater_trump_card):
                # if this a trump and we have a greater one, we must play higher or Fool
                return greater_trump_card + player_s_fool_card
            # else we must play a lower one or Fool (Fool has the lowest rank)
            return lower_trump_card
        elif Trump in owned_types:
            # if we don't have the asked type but have a Trump, we must play it
            return [card for card in not_played_cards if card.type == Trump]

    # if there is no typing card, we can play the card we want
    return not_played_cards
