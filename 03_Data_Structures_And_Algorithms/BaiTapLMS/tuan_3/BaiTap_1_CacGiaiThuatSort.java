public class BaiTap_1_CacGiaiThuatSort {
    /* BubbleSort: So sánh cặp và thay đổi vị trí nếu số sau < số trước */
    public static int[] BubbleSort(int arr[])
    {
        int temp[] = arr;
        for (int i = 0; i < temp.length - 1; i++)         
        {
            for (int j = i + 1; j < temp.length; j++)    
            {
                if (temp[j] < temp[i])
                {
                    int tempnum = temp[i];
                    temp[i] = temp[j];
                    temp[j] = tempnum;
                }
            }
        }
        return temp;
    }

    /* SelectionSort:
     * - Lấy điểm khởi đầu [0]
     * - Từ [1] -> [Cuối], tìm số nhỏ nhất
     * - Đổi vị trí điểm khởi đầu với số nhỏ nhất
     * - Tăng điểm khởi đầu lên 1
     */
    public static int[] SelectionSort(int arr[])
    {
        int temp[] = arr;
        int i;
        for (i = 0; i < temp.length - 1; i++)   // Điểm khởi đầu
        {
            int min = i;
            int j;
            for ( j = i + 1; j < temp.length; j++)  // Min
            {   
                if (temp[min] > temp[j])
                {
                    min = j;
                } 
            }
            int tempnum = temp[i];
            temp[i] = temp[min];
            temp[min] = tempnum;
        }
        return temp;
    }

    /* InsertionSort:
     * - Điểm khởi đầu [1], để giá trị vào temp
     * - Kiểm tra từ khởi đầu về tay trái, nếu bên trái > temp, đổi vị trí, thực hiện đến đầu mảng [0]
     */
    public static int[] InsertionSort(int arr[])
    {
        int temp[] = arr;
        for (int i = 1; i < temp.length - 1; i++)
        {
            int tempnum = temp[i];
            for (int j = i - 1; j >= 0; j--)
            {
                if (temp[j] > temp[i])
                {
                    temp[i] = temp[j];
                    temp[j] = tempnum;
                }
            }
        }

        return temp;
    }

    public static void main(String[] args) {
        int array[] = {3,5,9,6,8,1,2,7,4};

        int bubblesortarr[] = BubbleSort(array);
        int selectionsortarr[] = SelectionSort(array);
        int insertionsortarr[] = InsertionSort(array);
        
        for (int i : bubblesortarr)
        {
            System.out.print(i + " ");
        }
        System.out.println();

        
        for (int i : selectionsortarr)
        {
            System.out.print(i + " ");
        }
        System.out.println();

        
        for (int i : insertionsortarr)
        {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
