import java.util.Random;
import java.util.Scanner;

public class BaiTap_7_ReverseGuess {
    public static void main(String[] args) {
        try (Scanner console = new Scanner(System.in)) {
            Random r = new Random();

            int count = 1;
            int RandomNum = r.nextInt(10) + 1; // 1 -> 10
            String UserInput;

            System.out.println("Let me guess what your number!");

            System.out.print("Is it [" + RandomNum + "]? (Y/N) ");
            UserInput = console.next();

            while(!UserInput.equalsIgnoreCase("Y"))
            {
                count++;
                RandomNum = r.nextInt(10) + 1;
                System.out.print("Is it [" + RandomNum + "]? (Y/N) ");
                UserInput = console.next();
            }

            System.out.println("Got cha! I readed your mind in " + count + "time(s).");
        }
    }
}
