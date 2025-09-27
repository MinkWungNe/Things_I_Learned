public class Employee
{
    private int hour;
    private int salary;
    private int VacationDays;
    private String form;

    // Khởi tạo mặc định
    public Employee()   
    {
        this(40, 40000, 10, "yellow");    // 2 tuần nghỉ phép (không tính T7, CN)
    }

    // Khởi tạo có giá trị
    public Employee(int hour, int salary, int VacationDays, String form) 
    {
        this.hour = hour;
        this.salary = salary;
        this.VacationDays = VacationDays;
        this.form = form;
    }

    // Hàm lấy thông tin
    public int getHours() { return this.hour; }
    public int getSalary() { return this.salary; }
    public int getVacationDays() { return this.VacationDays; }
    public String getVacationForm() { return this.form; } 
}

// Bài Tập Số 1: viết lớp Employee
