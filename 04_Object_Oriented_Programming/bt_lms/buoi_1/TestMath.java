import java.util.Scanner; 
public class TestMath { 
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
        System.out.println("Enter 3 values: "); 
        double num1 = sc.nextDouble(); 
        double num2 = sc.nextDouble(); 
        double num3 = sc.nextDouble(); 
        System.out.println("Power of two numbers = " + Math.pow(num1, num2)); 
        double maxNumber= Math.max(Math.max(num1, num2), num3); 
        System.out.println("Largest = " + maxNumber); 
        System.out.println("Generating a random number: " + Math.random()); 
        System.out.printf("Number with 2 decimal places: %.2f", maxNumber);
    }
}