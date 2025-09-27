package bt_thuchanh.buoi_1.bai3;

public class AccountTest2 {
    public static void main(String[] args) {
        Account account1 = new Account("Nguyen Van A");
        Account account2 = new Account("Tran Van B");

        System.out.println("Account 1 ten la: " + account1.getName());
        System.out.println("Account 2 ten la: " + account2.getName());
    }
}
