public class BaiTap_1_SuDungClassPoint {
    public static void main(String[] args) {
        Point p = new Point();
        p.x = 10;
        p.y = 5;

        System.out.println("Gia tri truoc khi dich chuyen x: " + p.x + " y: " + p.y);
        
        p.Dich(2, 5);

        System.out.println("Gia tri sau khi dich chuyen x: " + p.x + " y: " + p.y);

        System.out.println("Khoang cach den goc toa do: " + p.KhoangCach());
    }
}
