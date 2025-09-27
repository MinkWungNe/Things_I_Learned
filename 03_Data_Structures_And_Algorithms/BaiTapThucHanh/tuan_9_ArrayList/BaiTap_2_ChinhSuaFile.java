import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class BaiTap_2_ChinhSuaFile {
    public static void main(String[] args) throws FileNotFoundException {
        String filePath = System.getProperty("user.dir") + File.separator + "speech.txt";
        Scanner console = new Scanner(new File(filePath));

        ArrayList<String> BannedWords = new ArrayList<>();
        BannedWords.add("one");
        BannedWords.add("a");
        BannedWords.add("to");
        BannedWords.add("time");
        BannedWords.add("of");
        BannedWords.add("in");

        while (console.hasNext())
        {   
            String result = console.next();
            if (BannedWords.contains(result))
            {
                System.out.println("Da tim thay tu bi Ban: " + result);
                console.remove();
            }
        }

        console.close();
    }
}
