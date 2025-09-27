import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BaiTap_5_DocFile {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner console = new Scanner(new File("tally.txt"));

        int counter[] = new int[5]; // Mảng chứa để đếm số

        // Chạy khi file còn số
        while (console.hasNextInt()) {
            int result = console.nextInt();
            counter[result]++;
        }

        System.out.println("Ket qua kiem tra file: ");
        for (int i = 0; i < counter.length; i++) {
            System.out.println(i + ": " + counter[i]);
        }

    }
}
