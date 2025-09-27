public class GradeBook {
    private String courseName;

    public GradeBook (String name) {
        this.courseName = name;
    }

    public void setCourseName(String name) {
        this.courseName = name;
    }

    public String getCourseName() {
        return courseName;
    }

    public void displayMessage() {
        System.out.printf("welcome to the grade book for \n%s!\n", getCourseName());
    }
}
