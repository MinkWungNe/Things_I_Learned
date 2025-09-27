import java.util.Scanner;

public class AccountTest {
    public static void main(String[] args) {
        Account account1 = new Account(50.00);
        Account account2 = new Account(-7.53);

        // print initalized accounts's balance
        System.out.printf("account1 balance: $%.2f\n", account1.getBalance());
        System.out.printf("account2 balance: $%.2f\n\n", account2.getBalance());

        Scanner input = new Scanner(System.in);
        double depositAmount;

        // Deposit for acccount1
        System.out.print("Enter deposit amount for account1: ");
        depositAmount = input.nextDouble();
        System.out.printf("\nadding %.2f to acccount1 balance\n\n", depositAmount);
        account1.credit(depositAmount);

        // print accounts's balance after updated account1
        System.out.printf("account1 balance: $%.2f\n", account1.getBalance());
        System.out.printf("account2 balance: $%.2f\n\n", account2.getBalance());

        // Deposit for acccount2
        System.out.print("Enter deposit amount for account2: ");
        depositAmount = input.nextDouble();
        System.out.printf("\nadding %.2f to acccount2 balance\n\n", depositAmount);
        account2.credit(depositAmount);

        // print accounts's balance after updated account2
        System.out.printf("account1 balance: $%.2f\n", account1.getBalance());
        System.out.printf("account2 balance: $%.2f\n\n", account2.getBalance());

        input.close();
    }
}
