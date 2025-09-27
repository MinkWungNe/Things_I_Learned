public class Lawyer extends Employee{   // Luật sư kế thừa trạng thái, hành vi Employee
    
    // Hàm khởi tạo mặc định
    public Lawyer()
    {
        super(40,40000,15, "pink"); // Luật sư có 15 ngày nghỉ phép
    }

    // Hàm khởi tạo có tham số
    public Lawyer(int hour, int salary) {
        super(hour, salary, 15, "pink"); 
    }

    // Hành vi đặc trưng
    public void hanhvirieng()
    {
        System.out.println("Toi biet cach xu ly cac vu kien!");
    }
    
}

// Bài tập 4-1: Viết lớp Lawyer, kế thừa Employee, có hơn 5 ngày nghỉ so với Employee