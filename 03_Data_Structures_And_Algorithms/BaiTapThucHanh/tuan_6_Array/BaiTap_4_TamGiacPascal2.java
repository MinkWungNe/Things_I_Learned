public class BaiTap_4_TamGiacPascal2 {
    public static void Initialize(int arr[][])
    {
        for (int i = 0; i < arr.length; i++)
        {
            arr[i] = new int[i + 1];    // arr[i] sẽ tạo thêm mảng với độ dài i + 1
            arr[i][0] = 1;  // Gia tri dau day
            arr[i][i] = 1;  // Gia tri cuoi day

            for (int j = 1; j < i; j++)
            {
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
            }
        }
    }

    public static void printSpace(int num)
    {
        for (int i = 1; i <= num; i++)
        {
            System.out.print("  ");
        }
    }

    public static void print(int tamgiac[][])
    {
        int spacenum = 10;
        for (int i = 0; i < tamgiac.length; i++)
        {   
            printSpace(spacenum);
            spacenum--;
            for (int j = 0; j < tamgiac[i].length;j++)
            {
                System.out.printf("%d",tamgiac[i][j]);
                if (tamgiac[i][j] <= 9)
                {
                    System.out.print("   ");
                }
                else if (tamgiac[i][j] <= 99)
                {
                    System.out.print("  ");
                }
                else 
                {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int tamgiac[][] = new int[6][];
        Initialize(tamgiac);
        print(tamgiac);
    }
}
