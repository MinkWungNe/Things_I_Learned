public class BTTHVN1 {
    public static void DrawV()
    {
        System.out.print("\\    /");System.out.print("   ");System.out.print("\\    /");System.out.print("   ");System.out.print("\\    /");System.out.print("   ");System.out.print("\\    /");System.out.print("   ");System.out.print("\\    /");System.out.println();
        System.out.print(" \\  / ");System.out.print("   ");System.out.print(" \\  / ");System.out.print("   ");System.out.print(" \\  / ");System.out.print("   ");System.out.print(" \\  / ");System.out.print("   ");System.out.print(" \\  / ");System.out.println();
        System.out.print("  \\/  ");System.out.print("   ");System.out.print("  \\/  ");System.out.print("   ");System.out.print("  \\/  ");System.out.print("   ");System.out.print("  \\/  ");System.out.print("   ");System.out.print("  \\/  ");System.out.println();
    }

    public static void DrawCone()
    {
        System.out.print ("  /\\  ");System.out.print("   ");System.out.print ("  /\\  ");System.out.print("   ");System.out.print ("  /\\  ");System.out.print("   ");System.out.print ("  /\\  ");System.out.print("   ");System.out.print ("  /\\  ");System.out.println();
        System.out.print (" /  \\ ");System.out.print("   ");System.out.print (" /  \\ ");System.out.print("   ");System.out.print (" /  \\ ");System.out.print("   ");System.out.print (" /  \\ ");System.out.print("   ");System.out.print (" /  \\ ");System.out.println();
        System.out.print ("/    \\");System.out.print("   ");System.out.print ("/    \\");System.out.print("   ");System.out.print ("/    \\");System.out.print("   ");System.out.print ("/    \\");System.out.print("   ");System.out.print ("/    \\");System.out.println();
    }

    public static void DrawBox()
    {
        System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.println();
        System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.println();
        System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.print("  ");System.out.print ("|     |");System.out.println();
        System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.print("  ");System.out.print ("+-----+");System.out.println();
    }

    public static void DrawX()
    {
        DrawV();
        DrawCone();
    }

    public static void DrawDiamond()
    {
        DrawCone();
        DrawV();
    }

    public static void DrawRocket()
    {
        DrawCone();
        DrawBox();
        System.out.print ("| Viet|");System.out.print("  ");System.out.print ("| Viet|");System.out.print("  ");System.out.print ("| Viet|");System.out.print("  ");System.out.print ("| Viet|");System.out.print("  ");System.out.print ("| Viet|");System.out.println();
        System.out.print ("|  Nam|");System.out.print("  ");System.out.print ("|  Nam|");System.out.print("  ");System.out.print ("|  Nam|");System.out.print("  ");System.out.print ("|  Nam|");System.out.print("  ");System.out.print ("|  Nam|");System.out.println();
        DrawBox();
        DrawCone();
    }

    public static void main(String[] args) {
        DrawDiamond(); 
        System.out.println();

        DrawX();   
        System.out.println();

        DrawRocket();  
    }
}
