import java.util.Scanner;

public class Lab2p1 {
    public static void main(String args[]) {
        int choice;
        Scanner sc = new Scanner(System.in);
        do {
        System.out.println("Perform the following methods:");
        System.out.println("1: multiplication test");
        System.out.println("2: quotient using division by subtraction");
        System.out.println("3: remainder using division by subtraction");
        System.out.println("4: count the number of digits");
        System.out.println("5: position of a digit");
        System.out.println("6: extract all odd digits");
        System.out.println("7: quit");
        choice = sc.nextInt();
        switch (choice) {
        case 1: mulTest();
        break;
        case 2: /* add divide() call */
        break;
        case 3: /* add modulus() call */
        break;
        case 4: /* add countDigits() call */
        break;
        case 5: /* add position() call */
        break;
        case 6: /* add extractOddDigits() call */
        break;
        case 7: System.out.println("Program terminating.......");
        }
        } while (choice < 7);
    }
        
    public static void mulTest() {

        Scanner scanner = new Scanner(System.in); 
        int correct = 0;

        for (int i = 1; i<=5; i++) {

            int max = 10;
            int min = 1;
            int range = max - min + 1;

        
            int first = (int)(Math.random() * range) + min;
            int second = (int)(Math.random() * range) + min;
            String prompt = String.format("How much is %d time %d? ", first, second);
            System.out.print(prompt);
            int answer = scanner.nextInt();
            if (answer == first * second) {
                correct += 1;
            }

        }
        String fin = String.format("%d answers out of 5 are correct. \n", correct);
        System.out.print(fin);
    }    
    /* 
    public static int divide(int m, int n) {

    }    
    
    public static int modulus(int m, int n) {

    }    

    
    public static int countDigits(int n) {

    }    
    
    public static int position(int n, int digit) {

    }    

    public static long extractOddDigits(int n, int digit) {

    }*/   
}
