// Principle of Inheritance, Fruit inherits from the Item class

public class Fruit extends Item {

    private String type;

    public Fruit(String type, String name, int quantity) {
        super(name, quantity);
        this.type = type;
    }

   public static void main(String[] var0) {
      System.out.println("Done");
   }
}
    
