package bt_thuchanh.buoi_1.bai4;

import java.util.Scanner;

public class AccountTest3 {

    public static void main(String[] args) {
        Account account1 = new Account(null, 50.0);
        Account account2 = new Account(null, 50.0);

        // Dat ten cho tk moi
        Scanner input = new Scanner(System.in);
        System.out.print("Account 1 chua co ten, moi nhap: ");
        String newName = input.nextLine();
        account1.setName(newName);

        System.out.print("Account 2 chua co ten, moi nhap: ");
        newName = input.nextLine();
        account2.setName(newName);

        // In thong tin
        System.out.println();
        System.out.println(account1.getName() + " co so du la: " + account1.getBalance());
        System.out.println(account2.getName() + " co so du la: " + account2.getBalance());

        // Cho user 1 deposit
        System.out.println();
        System.out.print("Nhap so can nap cho Account 1: ");
        double depositAmount = input.nextDouble();

        System.out.println("Ban dang cong them Account1 " + depositAmount);
        account1.deposit(depositAmount);

        //Check tai khoan sau khi nap
        System.out.println();
        System.out.println(account1.getName() + " co so du la: " + account1.getBalance());
        System.out.println(account2.getName() + " co so du la: " + account2.getBalance());

        // Cho user 2 deposit
        System.out.println();
        System.out.print("Nhap so can nap cho Account 2: ");
        depositAmount = input.nextDouble();

        System.out.println("Ban dang cong them Account2 " + depositAmount);
        account1.deposit(depositAmount);

        //Check tai khoan sau khi nap
        System.out.println();
        System.out.println(account1.getName() + " co so du la: " + account1.getBalance());
        System.out.println(account2.getName() + " co so du la: " + account2.getBalance());
        
        input.close();
    }
}
