import random

if __name__ == '__main__':
    import random

    # Define the deck of cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


    # Define functions for the game

    def create_deck():
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} of {suit}')
        return deck


    def shuffle_deck(deck):
        random.shuffle(deck)


    def deal_card(deck):
        return deck.pop()


    def calculate_hand_value(hand):
        value = sum(values[card.split()[0]] for card in hand)
        num_aces = sum(1 for card in hand if 'Ace' in card)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value


    def blackjack():
        print("Bienvenue au jeu de Blackjack!")

        deck = create_deck()
        shuffle_deck(deck)

        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        while True:
            player_score = calculate_hand_value(player_hand)
            dealer_score = calculate_hand_value(dealer_hand)

            print("\nVotre main:")
            for card in player_hand:
                print(card)
            print(f"Total de votre main: {player_score}\n")

            print("Main du croupier:")
            print(dealer_hand[0])  # Only show the dealer's first card
            print("\nQue souhaitez-vous faire?")
            print("1. Prendre une carte")
            print("2. Rester")

            choice = input("Votre choix: ")

            if choice == '1':
                player_hand.append(deal_card(deck))
            elif choice == '2':
                while dealer_score < 17:
                    dealer_hand.append(deal_card(deck))
                    dealer_score = calculate_hand_value(dealer_hand)
                break

            if player_score > 21:
                print("\nVous avez dépassé 21. Le croupier gagne!")
                return
            elif dealer_score > 21:
                print("\nLe croupier a dépassé 21. Vous gagnez!")
                return

        print("\nMain du croupier:")
        for card in dealer_hand:
            print(card)
        print(f"Total de la main du croupier: {dealer_score}")

        if player_score > dealer_score:
            print("\nVous avez gagné!")
        elif player_score < dealer_score:
            print("\nLe croupier a gagné!")
        else:
            print("\nC'est une égalité!")


    # Let us commence the game, mon ami!
    blackjack()
