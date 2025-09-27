import java.util.Scanner;

public class TestScanner {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter name1: ");
            String name1 = sc.nextLine();
            System.out.println("name1 entered is '" + name1 + "' .");

            System.out.print("Enter name2: ");
            String name2 = sc.next();
            System.out.println("name1 entered is '" + name2 + "' .");
        }
    }
}