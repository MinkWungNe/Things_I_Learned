import java.util.ArrayList;

public class BaiTap_1_TaoArrayList {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        String result;
        int result2;

        // 1) Tạo ArrayList
        list.add("Hoa");        // 0
        list.add("Mai");        // 1
        list.add("Dung");       // 2
        list.add("Hoang");      // 3
        list.add("Hai");        // 4
        list.add("Vinh");       // 5
        list.add("Tu");         // 6
        list.add("Bao");        // 7
        list.add("Anh");        // 8

        System.out.print("1) Tao ArrayList: ");
        for (int i = 0; i < list.size(); i++)
        {
            result = list.get(i);
            System.out.print(result + " ");
        }
        System.out.println();

        // 2) Thêm "Tung" vào giữa "Dung" và "Hoang"
        list.add(3, "Tung");

        System.out.print("2) Them \"Tung\" vao giua \"Dung\" va \"Hoang\": ");
        for (int i = 0; i < list.size(); i++)
        {
            result = list.get(i);
            System.out.print(result + " ");
        }
        System.out.println();

        // 3) Thêm cuối dãy "Oanh"
        list.add(list.size(), "Oanh");

        System.out.print("3) Them \"Oanh\" vao cuoi day: ");
        for (int i = 0; i < list.size(); i++)
        {
            result = list.get(i);
            System.out.print(result + " ");
        }
        System.out.println();

        // 4) Hiển thị giá trị dãy tại vị trí 7
        result = list.get(7);
        System.out.println("4) Gia tri tai vi tri 7: " + result);

        // 5) Hiển thị chiều dài của dãy trên
        result2 = list.size();
        System.out.println("5) Chieu dai day: " + result2);

        // 6) Xóa tên tại vị trí 3 và vị trí 6
        list.remove(3);
        list.remove(6);

        System.out.print("6) ArrayList sau khi xoa vi tri 3 va 6: ");
        for (int i = 0; i < list.size(); i++)
        {
            result = list.get(i);
            System.out.print(result + " ");
        }
        System.out.println();

        // 7) Thay thế tên vị trí 2 thành "Toang"
        list.set(2, "Toang");

        System.out.print("7) ArrayList sau khi thay the vi tri 2: ");
        for (int i = 0; i < list.size(); i++)
        {
            result = list.get(i);
            System.out.print(result + " ");
        }
        System.out.println();

        // 8) Hiển thị chiều dài của dãy
        result2 = list.size();
        System.out.println("8) Chieu dai day: " + result2);
    }
}
