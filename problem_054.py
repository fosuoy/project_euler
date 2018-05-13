#!/usr/bin/env python3
import time
import re


def blurb():
    print("""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD   2C 3S 8S 8D TD
Pair of Fives            Pair of Eights      Player 2
2	 	5D 8C 9S JS AC   2C 5C 7D 8S QH
Highest card Ace         Highest card Queen  Player 1
3	 	2D 9C AS AH AC   3D 6D 7D TD QD
Three Aces               Flush with Diamonds Player 2
4	 	4D 6S 9H QH QC   3D 6D 7H QD QS
Pair of Queens           Pair of Queens
Highest card Nine        Highest card Seven  Player 1
5	 	2H 2D 4C 4D 4S   3C 3D 3S 9S 9D
Full House               Full House
With Three Fours         with Three Threes   Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
    """)


def highest_card(hand):
    '''
    Just return the value of the highest card
    '''
    base_score = 14
    cards = list(hand.keys())
    return base_score - 14 + max(cards)


def is_one_pair(hand):
    '''
    If one pair is present return score
    '''
    base_score = 28
    for card, suite in hand.items():
        if len(suite) == 2:
            return base_score - 14 + card
    return 0


def is_two_pairs(hand):
    '''
    If two pairs are present return score
    '''
    base_score = 42
    pairs = []
    for card, suite in hand.items():
        if len(suite) == 2:
            pairs.append(card)
    if len(pairs) == 2:
        return base_score - 14 + max(pairs)
    return 0


def is_three_of_a_kind(hand):
    '''
    Three cards of the same value
    '''
    base_score = 56
    for card, suite in hand.items():
        if len(suite) == 3:
            return base_score - 14 + card
    return 0


def is_straight(hand):
    '''
    All cards are consecutive in values
    '''
    base_score = 70
    cards = list(hand.keys())
    if max(cards) - min(cards) == 4:
        return base_score - 14 + max(cards)
    return 0


def is_flush(hand):
    '''
    All cards have same suite
    return score base on highest card
    '''
    base_score = 84
    if len(set([x[0] for x in hand.values()])) == 1:
        return base_score - 14 + max(hand.keys())
    return 0


def is_full_house(hand):
    '''
    If the number of values is 2 and for those two cards there are 3 and 2
    suites then a full house is present
    '''
    base_score = 98
    if len(set(hand.keys())) == 2:
        number_of_suites = 5
        for key in hand.keys():
            number_of_suites -= len(hand[key])
        if number_of_suites == 0:
            return base_score
    return 0


def is_four_of_a_kind(hand):
    '''
    If there are only 2 different cards it means maybe there is 4 of a kind.
    If so then test if any card has 4 suites if so return score
    else return 0
    '''
    base_score = 112
    if len(set(hand.keys())) <= 2:
        for card, suite in hand.items():
            if len(suite) == 4:
                return base_score - 14 + card
    return 0


def is_straight_flush(hand):
    '''
    if all the values of the hand dictionary are the same it means all are the
    same suite.
    If the max card - the min card is 4 it means all numbers are consecutive
    '''
    base_score = 126
    if len(set([x[0] for x in hand.values()])) == 1:
        cards = list(hand.keys())
        if max(cards) - min(cards) == 4:
            return base_score
    return 0


def is_royal_flush(hand):
    '''
    If the list 10, 11, 12, 13, 14 is a subset of the keys of the hand
    dictionary it means the hand contains royal suite.
    Since there are only 5 cards in a hand make sure there is only one value for
    the set of values in the hand (meaning all cards are same suite), else
    return 0 score.
    '''
    base_score = 140
    if set(hand.keys()).issubset([10, 11, 12, 13, 14]):
        if len(set([x[0] for x in hand.values()])) == 1:
            return base_score
    return 0


def process_hand(hand):
    hand_dictionary = {}
    result = 0
    for card in hand:
        card_int = card[0]
        if card[0] == 'T':
            card_int = '10'
        elif card[0] == 'J':
            card_int = '11'
        elif card[0] == 'Q':
            card_int = '12'
        elif card[0] == 'K':
            card_int = '13'
        elif card[0] == 'A':
            card_int = '14'
        card_int = int(card_int)
        if card_int not in hand_dictionary.keys():
            hand_dictionary[card_int] = []
        hand_dictionary[card_int].append(card[1])
    result += is_royal_flush(hand_dictionary)
    result += is_straight_flush(hand_dictionary)
    result += is_four_of_a_kind(hand_dictionary)
    result += is_full_house(hand_dictionary)
    result += is_flush(hand_dictionary)
    result += is_straight(hand_dictionary)
    result += is_three_of_a_kind(hand_dictionary)
    result += is_two_pairs(hand_dictionary)
    result += is_one_pair(hand_dictionary)
    result += highest_card(hand_dictionary)
    return result


def player_one_win(game_hand):
    player_1_hand, player_2_hand = {}, {}
    player_1_hand_list = game_hand[0:15].split(" ")[0:5]
    player_2_hand_list = game_hand[15:30].split(" ")[0:5]
    player_1_hand = process_hand(player_1_hand_list)
    player_2_hand = process_hand(player_2_hand_list)
    if player_1_hand > player_2_hand:
        return True
    return False


def parse_poker_hands(poker_hands):
    '''
    Open the poker file then parse each line as it comes to figure out winner
    '''
    player_one_wins = 0
    with open(poker_hands, 'r') as f:
        for line in f:
            if player_one_win(line):
                player_one_wins += 1
    return player_one_wins



def main():
    blurb()
    start = time.time()
    RESULT = parse_poker_hands("problem_054_poker.txt")
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
