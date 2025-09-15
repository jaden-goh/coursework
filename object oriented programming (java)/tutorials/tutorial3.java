import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

// Outer class just to hold everything (normally you'd put each class in its own file)
public class tutorial3 {

    // ========== CLASS: Drink ==========
    // Encapsulation principle: each Drink hides its data (name, cost) behind private fields.
    public class Drink {
        private String name;
        private double cost;

        public Drink(String name, double cost) {
            this.name = name;
            this.cost = cost;
        }

        public String getName() {
            return this.name;
        }

        public double getCost() {
            return this.cost;
        }
    }

    // ========== CLASS: VendingMachine ==========
    // This class encapsulates the machine’s state (the menu, the money handling).
    // It is responsible for operations like adding drinks, selling, giving change.
    public class VendingMachine {
        private Map<String, Double> menu;

        // Constructor initializes the menu (ensuring machine starts in valid state).
        public VendingMachine() {
            menu = new HashMap<>();
        }

        // Encapsulation + abstraction:
        // Expose a safe public method to add drinks, 
        // but do not expose the menu directly.
        public void addDrink(Drink drink) {
            menu.put(drink.getName(), drink.getCost());
        }

        // Single Responsibility: this method only selects a drink and returns its cost.
        public double selectDrink() {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Available drinks:");
            for (String drinkName : menu.keySet()) {
                System.out.println("- " + drinkName + " ($" + menu.get(drinkName) + ")");
            }

            System.out.println("What drink would you like to have?");
            String drink = scanner.next();
            if (!menu.containsKey(drink)) {
                System.out.println("Sorry, that drink is not available.");
                return -1;
            }
            return menu.get(drink);
        }

        // This method simulates coin insertion until cost is met.
        // Abstraction: user deals with friendly coin labels, not raw numbers.
        public double insertCoins(double drinkCost) {
            double amount = 0;
            Scanner scanner = new Scanner(System.in);

            while (amount < drinkCost) {
                System.out.println("Insert coins: ");
                System.out.println("'Q' for 10 Cent");
                System.out.println("'T' for 20 Cent");
                System.out.println("'F' for 50 Cent");
                System.out.println("'N' for 1 Dollar");            
                char in = scanner.next().charAt(0);

                switch (in) {
                    case 'Q': amount += 0.10; break;
                    case 'T': amount += 0.20; break;
                    case 'F': amount += 0.50; break;
                    case 'N': amount += 1.00; break;
                    default: 
                        System.out.println("Invalid coin. Try again.");
                }

                System.out.printf("Total inserted: $%.2f\n", amount);
            }
            return amount;
        }

        // Cohesion: one method is responsible for giving change.
        public void checkChange(double amount, double drinkCost) {
            System.out.printf("Change: $%.2f\n", (amount - drinkCost));
        }

        // In a real system, this might write to a file or print a paper slip.
        public void printReceipt(String drinkName, double cost) {
            System.out.println("========== RECEIPT ==========");
            System.out.println("Drink: " + drinkName);
            System.out.printf("Cost: $%.2f\n", cost);
            System.out.println("Thank you for your purchase!");
            System.out.println("=============================");
        }
    }

    // ========== CLASS: VendingMachineApp ==========
    // This acts as the "driver" class (controller).
    // Principle of separation of concerns: 
    // It orchestrates interaction between user and VendingMachine, 
    // but does not manage coins/menu directly.
    public class VendingMachineApp {
        public void run() {
            VendingMachine machine = new VendingMachine();

            // Add some sample drinks
            machine.addDrink(new Drink("Coke", 1.50));
            machine.addDrink(new Drink("Water", 1.00));
            machine.addDrink(new Drink("Coffee", 2.00));

            // Flow: choose → pay → get change → print receipt
            double cost = machine.selectDrink();
            if (cost > 0) {
                double amountPaid = machine.insertCoins(cost);
                machine.checkChange(amountPaid, cost);
                machine.printReceipt("Your Drink", cost); // Here you’d ideally pass actual selection
            }
        }
    }
}
