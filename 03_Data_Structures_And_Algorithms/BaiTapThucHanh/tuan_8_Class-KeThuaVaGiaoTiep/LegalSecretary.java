public class LegalSecretary extends Employee{   // Thư ký pháp lý kế thừa hành vi, trạng thái Employee
    
    // Hàm khởi tạo mặc định
    public LegalSecretary() {
        super(40, 45000,10,"yellow"); // Gọi hàm khởi tạo mặc định của lớp Employee
    }

    // Hàm khởi tạo có tham số
    public LegalSecretary(int hour, int salary) {
        super(hour, salary,10, "yellow" ); // Thư ký có VacationDays và form giống Employee
    }

    // Hành vi đặc trưng
    public void hanhvirieng()
    {
        System.out.println("Toi biet cach nop ho so phap ly!");
    }


    public static void main(String[] args) {
        // Tạo đối tượng LegalSecretary với hàm khởi tạo mặc định
        LegalSecretary legalSecretary1 = new LegalSecretary();
        System.out.println("Legal Secretary 1:");
        System.out.println("Hours: " + legalSecretary1.getHours());
        System.out.println("Salary: " + legalSecretary1.getSalary());
        System.out.println("Vacation Days: " + legalSecretary1.getVacationDays());
        System.out.println("Vacation Form: " + legalSecretary1.getVacationForm());
        legalSecretary1.hanhvirieng(); // In ra "Tôi biết cách nộp hồ sơ pháp lý!"

        // Tạo đối tượng LegalSecretary với hàm khởi tạo có tham số
        LegalSecretary legalSecretary2 = new LegalSecretary(35, 50000);
        System.out.println("Legal Secretary 2:");
        System.out.println("Hours: " + legalSecretary2.getHours());
        System.out.println("Salary: " + legalSecretary2.getSalary());
        System.out.println("Vacation Days: " + legalSecretary2.getVacationDays());
        System.out.println("Vacation Form: " + legalSecretary2.getVacationForm());
        legalSecretary2.hanhvirieng(); // In ra "Tôi biết cách nộp hồ sơ pháp lý!"
    }
}

// Bài tập 4-2: Viết lớp LegalSecretary, kế thừa Employee, salary hơn 5000 so với Employee