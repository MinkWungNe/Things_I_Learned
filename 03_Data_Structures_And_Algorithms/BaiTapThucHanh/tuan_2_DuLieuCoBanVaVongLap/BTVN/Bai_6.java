public class Bai_6 {
    static void Line()
    {
        System.out.print("+");
        for(int i = 1; i <= 6; i++)
        {
            System.out.print("-");
        }
        System.out.println("+");
    }

    static void Up()
    {
        int i,j;
        for(i = 3; i >= 1; i--)
        {   
            System.out.print("|");
            for (j = 1; j <= i - 1; j++)
            {
                System.out.print(" ");
            }

            System.out.print("^");

            for(j = 5; j >= 2*i; j--)
            {
                System.out.print(" ");
            }

            System.out.print("^");

            for (j = 1; j <= i - 1; j++)
            {
                System.out.print(" ");
            }
            
            System.out.println("|");
        }
    }

    static void Down()
    {
        int i,j;
        for(i = 1; i <= 3; i++)
        {   
            System.out.print("|");
            for (j = 1; j <= i - 1; j++)
            {
                System.out.print(" ");
            }

            System.out.print("V");

            for(j = 5; j >= 2*i; j--)
            {
                System.out.print(" ");
            }

            System.out.print("V");

            for (j = 1; j <= i - 1; j++)
            {
                System.out.print(" ");
            }
            
            System.out.println("|");
        }
    }

    public static void main(String[] args) {
        Line();
        Up();
        Up();
        Line();
        Down();
        Down();
    }
}
