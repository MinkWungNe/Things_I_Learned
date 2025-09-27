import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class BaiTap_4_5_HashSet_DocFile {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner console = new Scanner(new File("mission.txt"));
        Set<String> set = new HashSet<>();
        List<String> list = new ArrayList<>();
        Set<String> words = new TreeSet<>(); // Bài 5

        while (console.hasNext())
        {   
            // 2
            String element = console.next();
            list.add(element);

            // 3
            set.add(element);

            // 4
            boolean isRepeated = Check(set, element);
            if (isRepeated)
            {
                System.out.println("Repeated word: " + element);
            }

            // Bài 5
            if (element.startsWith("a") && element.length() == 3)
            {
                words.add(element);
            }
        }

        System.out.println("Chieu dai file: " + list.size());   // In giá trị chiều dài của file
        System.out.println("Chieu dai HashSet: " + set.size()); // In giá trị chiều dài của HashSet

        // 5 
        System.out.println();
        System.out.println("HashSet: ");
        for (String result : set) {
            System.out.print(result + " ");
        }
        
        System.out.println();
        System.out.println();
        System.out.println("Three-letter \"a\" words: " + words);   // Bài 5
    }

    public static boolean Check(Set<String> set, String RepeatedString)
    {
        if (set.contains(RepeatedString))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
