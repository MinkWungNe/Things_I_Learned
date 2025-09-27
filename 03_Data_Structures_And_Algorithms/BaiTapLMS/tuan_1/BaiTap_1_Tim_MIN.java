import java.util.Scanner;

public class BaiTap_1_Tim_MIN {
    // BT: Tìm min trong 3 số
    public static void main(String[] args) {
        try (Scanner Input = new Scanner(System.in)) {
            int a, b, c, min;
            System.out.println("Nhap a: ");
            a = Input.nextInt();
            System.out.println("Nhap b: ");
            b = Input.nextInt();
            System.out.println("Nhap c: ");
            c = Input.nextInt();
            min = a;
            if(min > b)
            {
                min = b;
            }     if (min > c)
            {
                min = c;
            }     System.out.println("Gia tri nho nhat: " + min );
        }
    }
}