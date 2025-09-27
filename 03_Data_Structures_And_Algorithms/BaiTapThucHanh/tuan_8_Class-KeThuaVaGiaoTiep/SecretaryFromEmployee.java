public class SecretaryFromEmployee {
    private int hour;
    private int salary;
    private int VacationDays;
    private String form;

    public SecretaryFromEmployee(int hour, int salary, int VacationDays, String form) // Khởi tạo có giá trị
    {
        this.hour = hour;
        this.salary = salary;
        this.VacationDays = VacationDays;
        this.form = form;
    }

    public SecretaryFromEmployee()   // Khởi tạo mặc định
    {
        this(40, 40000, 10, "yellow");    // 2 tuần nghỉ phép (không tính T7, CN)
    }

    public int getHours() { return this.hour; }
    public int getSalary() { return this.salary; }
    public int getVacationDays() { return this.VacationDays; }
    public String getVacationForm() { return this.form; } 
    
    // Hành vi đặc trưng
    public void hanhvirieng()
    {
        System.out.println("Toi biet cach ghi chep!");
    }
}   

// Bài tập 2: Viết class Secretary bằng cách copy hành vi, trạng thái lớp Employee