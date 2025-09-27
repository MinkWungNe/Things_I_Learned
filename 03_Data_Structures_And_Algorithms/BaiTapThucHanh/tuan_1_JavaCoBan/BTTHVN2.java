public class BTTHVN2 {
    public static void DrawCap()
    {
        System.out.println("  *********  ");
        System.out.println(" *********** ");
        System.out.println("*************");
    }

    public static void DrawLine()
    {
        System.out.println("* | | | | | *");
    }

    public static void DrawLine2()
    {
        System.out.println("    *****   ");
    }

    public static void DrawPic0()
    {
        DrawCap();
    }

    public static void DrawPic1()
    {
        DrawCap();
        DrawLine();
        System.out.println("*************");
        DrawCap();
    }

    public static void DrawPic2()
    {
        DrawCap();
        DrawLine2();
        DrawLine();
        DrawLine();
        DrawLine2();
        DrawLine2();
    }

    public static void main(String[] args) {
        DrawPic0();
        System.out.println();
        DrawPic1();
        System.out.println();
        DrawPic2();
    }
}
