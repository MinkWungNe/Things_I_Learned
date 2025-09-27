public class Date {
    private int day;
    private int month;
    private int year;

    public Date(int day, int month, int year)
    {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public void addDays(int day)
    {
        this.day += day;
    }

    public void addWeeks (int week)
    {
        int dayToAdd = week * 7;
        for (int i = 0; i <= dayToAdd; i++)
        {
            if (day == 30)
            {
                month++;
                day = 0;
            }
            else{ day++;}
        }
    }

    public int daysTo(Date Other)
    {
        int OtherDay = Other.getDay();
        return Math.abs(day - OtherDay);
    }

    public int getDay() { return this.day;}
    public int getMonth() { return this.month;}
    public int getYear() { return this.year;}
    
    public boolean isLeapYear()  // Xảy ra mỗi 4 năm, trừ bội số 100 không phải bội số 400. (idk)
    {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public String ToString()
    {
        return this.year + "/" + this.month + "/" + this.day;
    }
}
