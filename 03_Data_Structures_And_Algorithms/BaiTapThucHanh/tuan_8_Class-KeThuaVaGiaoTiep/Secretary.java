public class Secretary extends Employee{    // 'extends Employee' để kế thừa trạng thái, hành vi của lớp Employee

    // Hàm khởi tạo mặc định
    public Secretary() {
        super(); // Gọi hàm khởi tạo mặc định của lớp Employee
    }

    // Hàm khởi tạo có tham số
    public Secretary(int hour, int salary) {
        super(hour, salary,10, "yellow" ); // Thư ký có VacationDays và form giống Employee
    }

    // Hành vi đặc trưng
    public void hanhvirieng()
    {
        System.out.println("Toi biet cach ghi chep!");
    }
}

// Bài tập 3: Viết lớp Secretary bằng phương pháp kế thừa
