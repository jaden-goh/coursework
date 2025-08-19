// Principle of Inheritance, Fruit inherits from the Item class

public class Fruit extends Item {

    private String type;

    public Fruit(String name, int quantity, String type) {
        super(name, quantity);
        this.type = type;

    }

    public String getType() {
        return type;
    }

    @Override
    public void displayInfo() {
        System.out.println("Item: " + getName() + ", Quantity: " + getQuantity() +  ", Type: " + type);
    
    }
   public static void main(String[] var0) {
      System.out.println("Done");
   }
}
    
