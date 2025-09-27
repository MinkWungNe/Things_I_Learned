import java.util.Scanner;

public class BaiTap_1_BinarySearch {
    // BT: Tìm 1 số trong mảng Theo thứ tự giảm dần bằng Binary Search
    public static int FindNum(int searchNum, int[] array)
    {
        int left = 0;
        int right = array.length - 1;

        while (true)
        {
            int mid = (left + right) / 2;

            if (array[mid] == searchNum)
            {
                return mid;
            }
            else if(left > right)
            {
                return 0;
            }
            else
            {
                if (array[mid] > searchNum)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }
        }
    }

    public static void main(String[] args) {
        int [] array = {9,8,7,6,5,4,3,2,1};
        int result, searchKey;
        try (Scanner input = new Scanner(System.in)) {
            System.out.println("Array: 9, 8, 7, 6, 5, 4, 3, 2, 1");
            System.out.print("Moi chon so can tim: ");
            searchKey = input.nextInt();
            
            result = FindNum(searchKey, array);
        }
        
        if ( result != 0)
        {
            System.out.println("Tim thay " + searchKey + " tai vi tri " + result + 1);
        }
        else
        {
            System.out.println("Khong tim thay!");
        }
    }
    
}
