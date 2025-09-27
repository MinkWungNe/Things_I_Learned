
import java.util.Scanner;

public class BaiTap_6_StillGuess {
    public static void main(String[] args) {
        int Ketqua = 42;
        int count = 0;
        int UserInput;
        try (Scanner console = new Scanner(System.in)) {
            System.out.println("Guess the number (dont worry we do got hints)");
            System.out.print("Answer: ");
            UserInput = console.nextInt();

            while (Ketqua != UserInput || UserInput >= 100)
            {
                int hint = 0;
                if((UserInput / 10 == Ketqua / 10) || (UserInput / 10 == Ketqua % 10))
                {
                    hint++;
                }
                if((UserInput % 10 == Ketqua / 10) || (UserInput % 10 == Ketqua % 10))
                {
                    hint++;
                }

                System.out.println("You got " + hint + "number right!");
                System.out.print("Again: ");
                UserInput = console.nextInt();
                count++;
            }
        }
        
        System.out.println("Correct! You Won!");
        System.out.println("Guess counted: " + count);
    }
}
