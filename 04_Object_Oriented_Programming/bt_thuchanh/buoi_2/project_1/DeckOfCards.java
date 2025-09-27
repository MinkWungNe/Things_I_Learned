package bt_thuchanh.buoi_2.project_1;

import java.security.SecureRandom;

public class DeckOfCards {
    private static int NUMBER_OF_CARDS = 52;
    private static final SecureRandom randomNumbers = new SecureRandom();
    private Card[] deck = new Card[NUMBER_OF_CARDS];
    private int currentCard = 0;

    // Initialize
    public DeckOfCards() {
        String[] faces = { "At", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin", "Muoi", "J", "Q", "K" };

        String[] suit = { "Co", "Ro", "Bich", "Nhep" };

        // Deck have 52 = Card (13*4)
        for (int count = 0; count < deck.length; count++) {
            deck[count] = new Card(faces[count % 13], suit[count / 13]);
        }
    }

    // Shuffle Method
    public void shuffle() {
        for (int first = 0; first < deck.length; first++) {
            int second = randomNumbers.nextInt(NUMBER_OF_CARDS); // Get random number to swap with

            Card temp = deck[first];
            deck[first] = deck[second];
            deck[second] = temp;
        }
    }

    // Deal Cards (chia bài)
    public Card dealCard() {
        if (currentCard < deck.length) {
            return deck[currentCard++];
        } else {
            return null;
        }
    }
}
