public class BaiTap_3_SuDungClassDate {
    public static void main(String[] args) {
        Date d1 = new Date(9, 2, 2005); // không nhuận
        Date d2 = new Date(2, 9, 2020); // nhuận

        int daysTo = d1.daysTo(d2);
        System.out.println("So ngay can dieu chinh: " + daysTo);

        boolean isLeapYear = d1.isLeapYear();   // false vì 2005 không nhuận
        if (isLeapYear)
        {
            System.out.println("Nam " + d1.getYear() + " la nam nhuan.");
        }
        else
        {
            System.out.println("Nam " + d1.getYear() + " khong la nam nhuan.");
        }

        String toDate = d1.ToString();
        System.out.println(toDate);
        d1.addWeeks(4);
        toDate = d1.ToString();
        System.out.println(toDate);
    }
}
