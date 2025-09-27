package bt_lms.buoi_2;

public class AnimalsTest {
    public static void main(String[] args) {
        Dog myDog = new Dog("Na", 120, 12, 5, true, "Chihuahua");
        Spider mySpider = new Spider("Man-Spider", 3, 50, 20, 8, false);

        myDog.eat("Noodle");
        myDog.move(20);
        myDog.bark();
        System.out.println(myDog.getAge());

        mySpider.eat("a man's remaining");
        mySpider.move(20);
        mySpider.setName("Venom");
        System.out.println(mySpider.getName());
    }
}
