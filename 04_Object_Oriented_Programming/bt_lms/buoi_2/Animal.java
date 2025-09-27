package bt_lms.buoi_2;

public class Animal {
    private String name;
    private int size;
    private int weight;
    private int age;

    public void setName(String name){
        this.name = name;
    }
    public void setSize(int size){
        this.size = size;
    }
    public void setWeight(int weight){
        this.weight = weight;
    }
    public void setAge(int age){
        this.age =age;
    }

    public String getName(){
        return name;
    }
    public int getSize(){
        return size;
    }
    public int getWeight(){
        return weight;
    }
    public int getAge(){
        return age;
    }

    public Animal(String name, int size, int weight, int age){
        this.name = name;
        this.size = size;
        this.weight = weight;
        this.age = age;
    }

    public void eat(String food){
        System.out.printf("The %s is eating %s!\n", getName(), food);
    }
    public void move(int velocity){
        System.out.printf("The %s is moving %s km/h!\n", getName(), velocity);
    }
}
