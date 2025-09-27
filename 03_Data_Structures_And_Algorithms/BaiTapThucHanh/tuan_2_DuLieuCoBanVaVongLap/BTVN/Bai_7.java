public class Bai_7 {
    static void Up()
    {
        int i,j;
        for (i = 4; i >= 1; i--)
        {
            System.out.print("|");

            for (j = 1; j <= i; j++)
            {
                System.out.print(" ");
            }

            for (j = 1; j <= ((5-1 * i) - 1); j++)
            {
                System.out.print("/");
            }
            
            System.out.print("*");

            for (j = 1; j <= ((5-1 * i) - 1); j++)
            {
                System.out.print("\\");
            }

            for (j = 1; j <= i; j++)
            {
                System.out.print(" ");
            }

            System.out.println("|");
        }
    }

    static void Down()
    {
        int i,j;
        for (i = 1; i <= 4; i++)
        {
            System.out.print("|");

            for (j = 1; j <= i; j++)
            {
                System.out.print(" ");
            }

            for (j = 1; j <= ((5-1 * i) - 1); j++)
            {
                System.out.print("\\");
            }
            
            System.out.print("*");

            for (j = 1; j <= ((5-1 * i) - 1); j++)
            {
                System.out.print("/");
            }

            for (j = 1; j <= i; j++)
            {
                System.out.print(" ");
            }

            System.out.println("|");
        }
    }

    static void Line()
    {
        System.out.print("+");
        for(int i = 0; i < 9; i++)
        {
            System.out.print("-");
        }
        System.out.println("+");
    }

    public static void main(String[] args) {
        Line();
        Up();
        Down();
        Line();
        Down();
        Up();
    }
}
