package bt_thuchanh.buoi_2.project_1;

public class DeckOfCardsTest {
    public static void main(String[] args) {
        DeckOfCards mydDeckOfCards = new DeckOfCards();
        mydDeckOfCards.shuffle();

        for (int i = 1; i <= 52; i++) {
            System.out.printf("%-19s", mydDeckOfCards.dealCard());

            // Create new line every 4 cards
            if (i % 4 == 0) {
                System.out.println();
            }
        }
    }
}
