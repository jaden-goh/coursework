

public class Main {
    
    public static void main(String[] args) {
        
        Inventory inventory = new Inventory();

        Fruit fruit1 = new Fruit("Strawberry", 5, "Blue");   
        Weapon weapon1 = new Weapon("Dagger", 1, "Persian", 50);

        inventory.addItem(fruit1);
        inventory.addItem(weapon1);

        inventory.displayInventory();


    }
}
