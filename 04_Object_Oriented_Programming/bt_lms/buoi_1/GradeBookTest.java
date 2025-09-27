import java.util.Scanner;

public class GradeBookTest {
    public static void main(String[] args) {
        GradeBook book1 = new GradeBook("OOP Java");
        GradeBook book2 = new GradeBook("DSA Java");

        System.out.printf("Gradebook1 course name is: %s\n", book1.getCourseName());
        System.out.printf("Gradebook2 course name is: %s\n", book2.getCourseName());
    }
}
