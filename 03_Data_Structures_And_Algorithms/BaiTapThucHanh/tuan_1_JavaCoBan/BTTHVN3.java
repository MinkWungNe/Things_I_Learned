public class BTTHVN3 {
    public static void DrawTop()
    {
        System.out.println("  _______  ");
        System.out.println(" /       \\");
        System.out.println("/         \\");
    }
    
    public static void DrawBottom()
    {
        System.out.println("\\         /");
        System.out.println(" \\_______/");
    }

    public static void StopSign()
    {
        DrawTop();
        System.out.println("|   STOP  |");
        DrawBottom();
    }

    

    public static void main(String[] args) {
        DrawTop();
        DrawBottom();
        DrawBottom();
        System.out.println(" +-------+");
        StopSign();
        DrawTop();
        System.out.println("+---------+");
    }
}
