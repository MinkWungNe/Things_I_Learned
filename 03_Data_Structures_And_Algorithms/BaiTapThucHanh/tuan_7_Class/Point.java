public class Point {
    int x;
    int y;

    public double KhoangCach()
    {
        return Math.sqrt(x*x + y*y);
    }

    public void Dich(int dx, int dy)
    {
        x += dx;
        y += dy;
    }
}
