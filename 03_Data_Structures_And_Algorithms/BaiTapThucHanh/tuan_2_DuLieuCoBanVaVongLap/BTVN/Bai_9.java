public class Bai_9 {
    public static void Space(int n)
    {
        for (int i = 0; i < n; i++)
        {
            System.out.print("     ");
        }
    }

    public static void StickMan(int part)
    {
        switch (part) {
            case 0 -> System.out.print("  .  ");
            case 1 -> System.out.print(" /|\\ ");
            case 2 -> System.out.print(" / \\ ");
            default -> {}
        }
    }
    
    public static void Draw(int num)
    {
        for (int i = 0; i < num; i++)
        {
            System.out.print("*");
        }
    }

    public static void main(String[] args) {
        int space_first = 4, space_last = 0;
        for (int i = 0; i <= 15; i++)
        {   
            if (i == 15)            // Hàng cuối
            {
                Draw(32);
                return;
            } 

            int space = i % 3;

            Space(space_first);     // Khoảng trống đầu

            StickMan(space);        // Vẽ người que

            if (space == 0)         // Vẽ cầu thang
            {
                Draw(6);
                Space(space_last);
            }
            else if (space == 1 || space == 2)
            {
                Draw(1);
                Space(space_last + 1);
            }
            
            Draw(1);            // Kết thúc hàng
            
            if (space == 2)         // Điều chỉnh khoảng cách đầu và cuối
            {
                space_first--;
                space_last++;
            }
            System.out.println();
        }
    }
}
