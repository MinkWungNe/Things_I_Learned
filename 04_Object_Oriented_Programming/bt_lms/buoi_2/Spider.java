package bt_lms.buoi_2;

public class Spider extends Animal{
    private int legs;
    private boolean poison;

    public void setLegs(int legs){
        this.legs = legs;
    }

    public void setPoison(boolean poison){
        this.poison = poison;
    }

    public boolean isPoison(){
        return poison;
    }
    public int getLegs(){
        return legs;
    }

    public Spider(String name, int size, int weight, int age, int legs, boolean poison){
        super(name, size, weight, age);
        this.legs = legs;
        this.poison = poison;
    }

    public void attack(){
        System.out.println("The spider is attacking!");
    }
}
