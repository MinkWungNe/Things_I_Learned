
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class BaiTap_5_Votes {
    public static void main(String[] args) throws FileNotFoundException{
        ArrayList<String> UngVien = new ArrayList<>();
        ArrayList<String> PhieuBau = new ArrayList<>();
        String filePath = "phieu.txt";
        try (Scanner console = new Scanner(new File(filePath))) {
            while (console.hasNext())
            {
                String name = console.next();
                PhieuBau.add(name);

                // Bổ sung tên ứng viên nếu chưa có
                if (!UngVien.contains(name))    
                {
                    UngVien.add(name);
                }
            }
        }

        System.out.println("list = " + UngVien);

        // Sort tên ứng viên
        Collections.sort(UngVien);

        // Đếm phiếu
        int VotesCount[] = new int[4];

        for (int i = 0; i < PhieuBau.size(); i++)
        {
            if (PhieuBau.get(i).equals("A"))
            {
                VotesCount[0]++;
            }
            if (PhieuBau.get(i).equals("B"))
            {
                VotesCount[1]++;
            }
            if (PhieuBau.get(i).equals("C"))
            {
                VotesCount[2]++;
            }
            if (PhieuBau.get(i).equals("D"))
            {
                VotesCount[3]++;
            }
        }

        // Hiển thị kết quả
        System.out.println("Ung vien" + "    " + "So phieu" + "    " + "Ty le bau (%)");
        for (int i = 0; i < UngVien.size(); i++)
        {
            double Votes = PhieuBau.size() / UngVien.size();
            double Percentage = (Votes / PhieuBau.size()) * 100;
            System.out.println("   " + UngVien.get(i) + "   " + "        " + VotesCount[i] + "             " + Percentage + "%");
        }
        System.out.println("Nguoi chien thang la: " + "all");
    }
}
