public class BaiTap_2_SuDungClassPoint2 {
    public static void main(String[] args) {
        Point2 p = new Point2(5,6);

        System.out.println("Gia tri truoc khi dich chuyen: " + p.ToString());
        
        p.Dich(1, 5);

        System.out.println("Gia tri sau khi dich chuyen: " + p.ToString());

        System.out.println("Khoang cach den goc toa do: " + p.KhoangCach());
    }
}
