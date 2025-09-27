import java.util.Random;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class BaiTap_7_SoXoKienThiet {
    public static void main(String[] args) {
        // 1) Chọn 6 số Random từ 1-40
        Set<Integer> Setwin = new TreeSet<>(RandomNum());

        // 2) Người dùng nhập 6 số bất kỳ
        Set<Integer> Setchon = new TreeSet<>(UserChoices());

        // 3) Tìm intersection của Setwin và SetChon
        Set<Integer> Sogiongnhau = new TreeSet<>(KiemTraKetQuaSoXoKienThiet(Setwin, Setchon));
        int same = Sogiongnhau.size();

        // 4) Tính tiền thưởng
        int TienThuong = same * 100;

        // 5) Hiển thị
        System.out.print("Setwin: " + Setwin);
        System.out.println("Setchon: " + Setchon);
        System.out.println("So giong nhau: " + Sogiongnhau);
        System.out.println("Tien thuong: " + TienThuong + " USD");
    }

    public static Set<Integer> RandomNum()
    {
        Set<Integer> temp = new TreeSet<>();
        Random r = new Random();
        for (int i = 0; i < 6; i++)
        {
            int randomNum = r.nextInt(1, 40);
            temp.add(randomNum);
        }

        return temp;
    }

    public static Set<Integer> UserChoices()
    {
        Set<Integer> temp = new TreeSet<>();
        System.out.println("Moi chon 6 so: ");
        try (Scanner console = new Scanner(System.in)) {
            for (int i = 0; i < 6; i++)
            {   
                System.out.print( (i + 1) + ": ");
                int input = console.nextInt();
                temp.add(input);
            }
        }
        return temp;
    }

    public static Set<Integer> KiemTraKetQuaSoXoKienThiet(Set<Integer> Setwin, Set<Integer> Setchon)
    {
        Set<Integer> intersect = new TreeSet<>(Setwin);
        intersect.retainAll(Setchon);
        return intersect;
    }
}
