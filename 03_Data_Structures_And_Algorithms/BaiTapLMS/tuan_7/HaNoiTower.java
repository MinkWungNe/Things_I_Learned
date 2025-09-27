public class HaNoiTower {
    // Đệ quy giải bài toán Tháp Hà Nội
    static void chuyenDia(int n, char cotNguon, char cotDich, char cotTrungGian) {
        if (n == 1) {
            System.out.println("Chuyển đĩa 1 từ " + cotNguon + " sang " + cotDich);
            return;
        }
        chuyenDia(n - 1, cotNguon, cotTrungGian, cotDich);
        System.out.println("Chuyển đĩa " + n + " từ " + cotNguon + " sang " + cotDich);
        chuyenDia(n - 1, cotTrungGian, cotDich, cotNguon);
    }

    public static void main(String[] args) {
        int soDia = 3; // Số đĩa
        chuyenDia(soDia, 'A', 'C', 'B'); // A, B và C là tên các cột
    }

}
