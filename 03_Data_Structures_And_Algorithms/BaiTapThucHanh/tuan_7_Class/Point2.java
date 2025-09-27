public class Point2 {
    private int x;
    private int y;

    public Point2() // Khởi tạo rỗng | Initialize without data
    {
        x = 0;
        y = 0;
    }

    public Point2(int x, int y) // Khởi tạo có đầu vào | Initialize with data
    {
        this.x = x; // this.x ý chỉ tới biến x của class, còn x là tham số. 
        this.y = y; // Có thể để biến x, y trong () ở dòng trên thành a, b, xong ghi x = a; y = b cũng được
    }

    public double KhoangCach()
    {
        return Math.sqrt(x*x + y*y);
    }

    public int getX() { return this.x; }
    public int getY() { return this.y; }

    public void setLocation(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public String ToString()
    {
        return "(" + x + "," + y + ")";
    }

    public void Dich(int x, int y)
    {
        this.x += x;
        this.y += y;
    }
}
