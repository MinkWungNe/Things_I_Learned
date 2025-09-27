
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class BaiTap_3_SieveOfEratosthenes {
    public static void main(String[] args) {
        // 1) Tạo dãy liên tục (2 -> 25)
        List<Integer> list = Initialize(2, 25);
        List<Integer> soNguyenTo = new LinkedList<>();
        PrintList(list, "Day so");
        PrintList(soNguyenTo, "So Nguyen To");

        while (!list.isEmpty())
        {   
            int PrimeNum = GetPrime(list, soNguyenTo);
            Clean(list, PrimeNum);
            PrintList(list, "Day so");
            PrintList(soNguyenTo, "So Nguyen To");
            System.out.println();
        }

    }

    // Tạo dãy số
    public static List<Integer> Initialize(int Start, int Max)
    {
        List<Integer> tempList = new LinkedList<>();

        for (int i = Start; i <= Max; i++)
        {
            tempList.add(i);
        }

        return tempList;
    }

    // Lấy số nguyên tố
    public static int GetPrime(List<Integer> list, List<Integer> soNguyenTo)
    {   
        soNguyenTo.add(list.get(0));
        return list.get(0);
    }

    // Xóa bớt các số chia hết cho số nguyên tố
    public static void Clean(List<Integer> list, int Prime)
    {
        Iterator<Integer> i = list.iterator();
        while(i.hasNext())  // loop tới rỗng
        {
            int element = i.next();
            if (element % Prime == 0)
            {
                i.remove();
            }
        }
    }

    // Print
    public static void PrintList(List<Integer> list, String ListName)
    {   
        System.out.print("[" + ListName + "]: ");   // In tên List
        Iterator<Integer> i = list.iterator();
        while (i.hasNext())
        {
            int element = i.next();
            System.out.print(element + " ");
        }
        System.out.println();
    }
}
