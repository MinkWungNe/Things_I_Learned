
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BaiTap_4_ArrayListSort {
    public static void main(String[] args) {
        ArrayList<String> words = new ArrayList<>(List.of("four", "score", "and", "seven", "years", "ago"));

        System.out.print("ArrayList truoc khi sort: ");
        for (int i = 0; i < words.size(); i++)
        {
            System.out.println(words.get(i));
        }

        Collections.sort(words);

        System.out.print("ArrayList sau khi sort: ");
        for (int i = 0; i < words.size(); i++)
        {
            System.out.println(words.get(i));
        }
    }
}
