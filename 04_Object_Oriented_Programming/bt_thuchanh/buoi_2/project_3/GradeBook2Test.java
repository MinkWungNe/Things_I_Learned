package bt_thuchanh.buoi_2.project_3;

public class GradeBook2Test {
    public static void main(String[] args) {
        int[][] gradesArray = {
            {87, 96, 70},
            {68, 87, 90},
            {94, 100, 90},
            {100, 81, 82}, 
            {83, 65, 85},
            {78, 87, 65},
            {85, 75, 83},
            {91,94, 100},
            {76, 72, 84},
            {87, 93, 73}
        };

        GradeBook2 myGradeBook2 = new GradeBook2("Lap trinh huong doi tuong", gradesArray);

        System.out.printf("Bang diem cho mon hoc %n%s%n%n", myGradeBook2.getCouseName());

        myGradeBook2.processGrades();
    }
}
