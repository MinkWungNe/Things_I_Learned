import java.util.ArrayList;
import java.util.List;

public class BaiTap_3_TinhTong {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>(List.of(13, 47, 15, 9, 5, 2, 89));
        int sum = 0;
        
        for (int i = 0; i < list.size(); i++)
        {
            sum += list.get(i);
        }
        System.out.println("Sum = " + sum);
    }
}
