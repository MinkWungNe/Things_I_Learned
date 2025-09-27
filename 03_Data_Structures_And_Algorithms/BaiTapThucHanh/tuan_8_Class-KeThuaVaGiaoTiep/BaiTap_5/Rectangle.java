public class Rectangle implements Shape{
    private double width;
    private double height;

    // Khởi tạo mặc định
    public Rectangle()
    {
        this.width = 0;
        this.height = 0;
    }

    // Khởi tạo có giá trị
    public Rectangle(double width, double height)
    {
        this.width = width;
        this.height = height;
    }
    
    @Override   
    public double getArea()
    {
        return this.width*this.height;
    }

    @Override   
    public double getPerimeter()
    {
        return 2*(this.width + this.height);
    }
}

/*  Note: Ghi @Override cho trình biên dịch biết phương thức nào đang ghi đè một phương thức trong lớp cha. 
 *  Annotations có thể được xử lý ở thời gian biên dịch hoặc thời gian chạy.
 */

 // Bài tập 5: Viết chương trình tính Chu vi, Diện tích của hình vuông, hình tròn, tam giác bằng phương pháp 