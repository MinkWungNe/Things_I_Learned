package bt_thuchanh.buoi_2.project_1;
public class Card {
    private final String face;
    private final String suit;

    public Card(String cardFace, String cardSuit) {
        this.face = cardFace;
        this.suit = cardSuit;
    }

    public String toString() {
        return face + " of " + suit;
    }
}
