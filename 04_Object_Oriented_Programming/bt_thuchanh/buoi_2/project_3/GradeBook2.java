package bt_thuchanh.buoi_2.project_3;

public class GradeBook2 {
    private String courseName;
    private final int[][] grades;

    public GradeBook2(String courseName, int[][] grades) {
        this.courseName = courseName;
        this.grades = grades;
    }

    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }

    public String getCouseName() {
        return courseName;
    }

    public void processGrades() {
        outputGrades();

        System.out.printf("Lowest grade is %d%nHighest grade is %d%n%n", getMinimum(), getMaximum());

        outputBarChart();
    }

    public int getMinimum() {
        int lowGrade = grades[0][0];
        for (int[] studentGrades : grades) {
            for (int grade : studentGrades) {
                if (grade < lowGrade) {
                    lowGrade = grade;
                }
            }
        }
        return lowGrade;
    }

    public int getMaximum() {
        int highGrade = grades[0][0];
        for (int[] studentGrades : grades) {
            for (int grade : studentGrades) {
                if (grade > highGrade) {
                    highGrade = grade;
                }
            }
        }
        return highGrade;
    }

    public double getAverage(int[] setOfGrades) {
        int total = 0;
        for (int grade : setOfGrades) {
            total += grade;
        }

        return (double) total / grades.length;
    }

    public void outputGrades() {
        System.out.printf("The grades are:%n%n");
        System.out.println("            ");

        for (int test = 0; test < grades[0].length; test++) {
            System.out.printf("Kiem tra %d:", test + 1);
        }

        // Average collum
        System.out.println("Average");

        for (int student = 0; student < grades.length; student++) {
            // collum 1: Student's name
            System.out.printf("Student %2d", student + 1);

            // display grade
            for (int test : grades[student]) {
                System.out.printf("%12d", test);
            }

            // display student's average grade
            double avarage = getAverage(grades[student]);
            System.out.printf("   %9.2f%n", avarage);
        }
    }

    public void outputBarChart() {
        System.out.println("Pho diem:");

        // Create an array with the size of 11
        int[] frequency = new int[11];
        
        // Calculate the frequency
        for (int[] studentGrades : grades) {
            for (int grade : studentGrades) {
                ++frequency[grade / 10];
            }
        }

        // DisplayChart
        for (int count = 0; count < frequency.length; count++) {
            if (count == 10) {
                System.out.printf("%5d:" , 100);
            }
            else {
                // start from _0 -> _9
                System.out.printf("%02d-%02d:", count + 10, count * 10 + 9);
            }

            for (int stars = 0; stars < frequency[count]; stars++) {
                System.out.print("*");
            }
            System.out.println();   // New line for new range
        }

        
    }
}
