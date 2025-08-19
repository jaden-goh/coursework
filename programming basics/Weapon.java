public class Weapon extends Item{

    private String type;
    private int damage;

    public Weapon(String name, int quantity, String type, int damage) {
        super(name, quantity);
        this.type = type;
        this.damage = damage;

    }

    public String getType() {
        return type;
    }
    public int getDamage() {
        return damage;
    }
    
    public static void main(String[] var0) {
      System.out.println("Done");
   }
}
