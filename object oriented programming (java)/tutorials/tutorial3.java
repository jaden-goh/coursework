import java.util.Map;
import java.util.Scanner;

public class tutorial3 {
    public class VendingMachine {
        private Map<String, Double> menu;
        
        public VendingMachine() {}

        public void addDrink(Drink drink) {
            menu.put(drink.name, drink.cost);
        }

        public double selectDrink() {
            Scanner scanner = new Scanner(System.in);
            System.out.println("What drink would you like to have?");
            String drink = scanner.next();
            double cost = menu.get(drink);
            return cost;
        }

        public double insertCoins(double drinkCost) {
            double amount = 0;
            while (drinkCost >= 0) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Insert Money: ");
            double in = scanner.nextDouble();
            drinkCost -= in;
            amount += in;}
            return amount;
        }

        public void checkChange(double amount, double drinkCost) {
            System.out.printf("Change: $%.2f", (amount-drinkCost));
        }

        public void printReceipt() {
            System.out.println("Receipt: ????????????????????");
        }
    }
    
    public class Drink {
        private String name;
        private double cost;
        
        public Drink(String name, double cost) {
            this.name = name;
            this.cost = cost;
        }

    }

    public class VendingMachineApp {
        public VendingMachineApp() {
            


        }
    }
}

