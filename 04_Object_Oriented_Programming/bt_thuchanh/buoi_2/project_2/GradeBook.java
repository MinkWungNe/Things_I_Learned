package bt_thuchanh.buoi_2.project_2;

public class GradeBook {
    private String courseName;
    private int[] grades;

    // Initialize
    public GradeBook(String courseName, int[] grades) {
        this.courseName = courseName;
        this.grades = grades;
    }

    // Set name for courses 
    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }

    public String getCourseName() {
        return courseName;
    }

    public void procesGrades() {
        outputGrades();
        System.out.printf("%nClass avarage is %.2f%n", getAverage());

        System.out.printf("Lowest grade is %d%nHighest grade is %d%n%n", getMinimum(), getMaximum());

        outputBarChart();
    }

    public int getMinimum() {
        int lowGrade = grades[0];
        for (int grade : grades) {
            if (grade < lowGrade) {
                lowGrade = grade;
            }
        }
        return lowGrade;
    }
    
    public int getMaximum() {
        int highGrade = grades[0];
        for (int grade : grades) {
            if (grade > highGrade) {
                highGrade = grade;
            }
        }
        return highGrade;
    }

    public double getAverage() {
        int total = 0;
        for (int grade : grades) {
            total += grade;
        }

        return (double) total / grades.length;
    }

    public void outputGrades() {
        System.out.printf("The grades are:%n%n");
        for (int student = 0; student < grades.length; student++) {
            System.out.printf("Student %2d: %3d%n", student + 1, grades[student]);
        }
    }

    public void outputBarChart() {
        System.out.println("Pho diem:");

        // Create an array with the size of 11
        int[] frequency = new int[11];
        
        // Calculate the frequency
        for (int grade :grades) {
            ++frequency[grade / 10];
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
