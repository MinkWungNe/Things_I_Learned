package bt_thuchanh.buoi_3.baitap_1;

public class Time1Test {
    public static void main(String[] args) {
        Time1 time = new Time1();

        displayTime("Truoc khi cai dat thoi gian", time);
        System.out.println();

        time.setTime(13, 27, 6);
        displayTime("Sau khi cai dat thoi gian", time);
        System.out.println();

        try {
            time.setTime(99, 99, 99);
        } catch (IllegalArgumentException c) {
            System.out.printf("Canh bao: %s%n%n", c.getMessage());
        }

        displayTime("Sau khi thiet lap thoi gian sai", time);
    }

    private static void displayTime(String header, Time1 t) {
        System.out.printf("%s%nUniversal time: %s%nStandard time: %s%n", header, t.toUniversalString(), t.toString());
    }
}
