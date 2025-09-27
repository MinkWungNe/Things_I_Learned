public class Bai_8 {
    static void Line()
    {
        System.out.print("|");
        for(int i = 0; i < 10; i++)
        {
            System.out.print("\"");
        }
        System.out.println("|");
    }

    static void Top()
    {
        int i,j;
        for(i = 1; i <= 4; i++)
        {
            for (j = 1; j <= i; j++)
            {
                System.out.print(" ");
            }

            System.out.print("\\");

            for(j = 0; j < (10-2 * i); j++)
            {
                System.out.print(":");
            }
            System.out.println("/");
        }
    }

    static void Bottom()
    {
        int i,j;
        for(i = 4; i >= 1; i--)
        {
            for (j = 1; j <= i; j++)
            {
                System.out.print(" ");
            }

            System.out.print("/");

            for(j = 0; j < (10-2 * i); j++)
            {
                System.out.print(":");
            }
            System.out.println("\\");
        }
    }

    public static void main(String[] args) {
        Line();
        Top();
        System.out.println("     ||    ");
        Bottom();
        Line();
    }
}
