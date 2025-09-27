import java.util.Scanner;

public class BaiTap_1_TinhNhietDo {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int days;
        double sum = 0;
        double average;

        System.out.print("Ban muon nhap nhiet do bao nhieu ngay?: ");
        days = console.nextInt();

        for (int i = 0; i < days; i++)
        {
            System.out.print("Nhiet do ngay thu " + (i + 1) + ": ");
            int input = console.nextInt();
            System.out.println();
            sum += input;
        }
        average = sum / days;

        for (int i = 0; i < days; i++)
        {
            System.out.print("Nhiet do trung binh: " + average);
        }

    }
}
