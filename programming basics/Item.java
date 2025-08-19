// Abstraction: the abstract method makes it such that people cannot create generic nonsense items and only items that fit one of the child classes
public abstract class Item {
    
    // Encapsulation: name and quantity are not accessible outside by any method other than the ones we defined.

    private String name;
    private int quantity;

    public Item(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
    }
    public String getName() {
        return this.name;
    }
    public int getQuantity() {
        
        return this.quantity;
    }

    public abstract void displayInfo();

    public static void main(String[] args) {
        System.out.println("Done");
}
}