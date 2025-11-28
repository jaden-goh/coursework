import java.awt.*;
import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Scanner;

public class basics {

    public static void main(String[] args) {
        // Basic Variable Types
        int age = 30; // -2,147,483,648 to 2,147,483,647, 32 bit
        byte height = 121; // -128 to 127 value, 8bit
        // short: -32768 to 32767 value, 16bit 
        long creditCard = 12345678910L; // -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 , 64 bit
        String name = "Bro"; 
        boolean single = true;
        float money = 10.11F;
        double weight = 100.45;
        System.out.println(++age + "\n" + name);
        System.out.println(age);

        // Reference Variables
        Point point1 = new Point(1, 1);
        Point point2 = point1;
        point1.x = 2;
        System.out.println(point1);
        System.out.println(point2);

        // Arrays
        int[] numberArray = new int[5];
        numberArray[0] = 1;
        numberArray[4] = 2;
        System.out.println(Arrays.toString(numberArray));
        
        // Multi Arrays
        int[][][] multiArray = new int[3][3][3];
        multiArray[1][1][1] = 123;
        System.out.println(Arrays.deepToString(multiArray));

        // Arithmetic Expressions
        double ratio = (double) weight / (double)height;
        float moneyPlus = ++money;
        System.out.println(moneyPlus);
        
        // Casting
        String inputstring = "13";
        int inputint = Integer.parseInt(inputstring) + 2;
        System.out.println(inputint);

        // Math class (round, max, min, random etc.)
        System.out.println(Math.round(money));

        // Number formatting, specific functions to convert numbers to certain formats
        NumberFormat currency = NumberFormat.getCurrencyInstance(); // define the formatting operation
        String result = currency.format(1234567.89);
        System.out.println(result);

        String percent = NumberFormat.getPercentInstance().format(0.12542); // alternatively, just put the number you want formatted in the instantiation
        System.out.println(percent);

        // Reading Input
        System.out.print("Input your age: ");
        Scanner scanner = new Scanner(System.in); // scanner is your variable where it takes in an input such as in Python: name = input("Enter your name: ") 
        byte ana_age = scanner.nextByte();
        System.out.println("You're " + ana_age + "????");

         // Logical Operators && and, || or, ==, >, <, !=
        int temperature = 31;
        boolean isWarm = temperature > 20 && temperature < 30;
        System.out.println(isWarm);

        // if statements
        if (isWarm == true) {
            System.out.println("Nice weather we got"); }
        else if (isWarm == false) {
            System.out.println("Mannnnn"); }

        System.out.printf("%-4.2f", 19.779);
    }
}
