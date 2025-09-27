public class Circle implements Shape{
    private double r;

    // Khởi tạo mặc định
    public Circle()
    {
        this.r = 0;
    }

    // Khởi tạo có giá trị
    public Circle(double r)
    {
        this.r = r;
    }
    
    @Override   
    public double getArea()
    {
        return Math.PI * (r*r);
    }

    @Override   
    public double getPerimeter()
    {
        return 2 * Math.PI * r;
    }
}
