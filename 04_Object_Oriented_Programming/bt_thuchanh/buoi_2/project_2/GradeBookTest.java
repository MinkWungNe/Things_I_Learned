package bt_thuchanh.buoi_2.project_2;

public class GradeBookTest {
    public static void main(String[] args) {
        int[] gradesArray = {87, 68, 94, 100, 83, 78, 85, 91, 76, 87};

        GradeBook myGradeBook = new GradeBook("Lap trinh huong doi tuong", gradesArray);

        System.out.printf("Bang diem cho mon hoc%n%s%n%n", myGradeBook.getCourseName());

        myGradeBook.procesGrades();
    }
}
