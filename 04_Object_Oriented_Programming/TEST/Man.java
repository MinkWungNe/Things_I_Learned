class Student {
    public int getAge() {
    return 10;
    }
    }
    public class Man extends Student {
    public int getAge(int added) {
    return super.getAge() + added;
    }
    public static void main(String[] args) {
    Man s = new Man();
    System.out.println(s.getAge());
    System.out.println(s.getAge());
    }
    }