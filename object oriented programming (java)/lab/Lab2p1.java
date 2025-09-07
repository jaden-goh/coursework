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
    
    public static int divide(int m, int n) {
        int ans = m / n;
        String answer = String.format("%d %% %d = %d", m, n, ans);
        System.out.print(answer); 
        return ans;  
    }    

    public static int modulus(int m, int n) {
        int ans = m % n;
        String answer = String.format("%d %% %d = %d", m, n, ans);
        System.out.print(answer); 
        return ans;  
    }    
    
    public static int countDigits(int n) {
        
        if (n > 0) {
            String nString = String.valueOf(n);
            int L = nString.length();
            String answer = String.format("n: %d - count = %d", n, L);
            System.out.print(answer);
            return n; 
        }
        else {
            String answer = String.format("n: %d - Error input!!", n);
            System.out.print(answer); 
            return n; 
        }

    }    
    
    public static int position(int n, int digit) {
        if (n > 0) {
            int pos = 1;
            while (n > 1) {
                if (n % 10 == digit) {
                    return pos;
                }
                else {
                    n = n / 10;
                    pos++;
                }
            }
            return -1;
        }
        else {
            String answer = String.format("n: %d - Error input!!", n);
            System.out.print(answer); 
            return n; 
        }
    }    

    public static long extractOddDigits(int n, int digit) {
        if (n > 0) {

            Double ans = 0;
            Double pos = 0;
            while (n > 1) {
                if ((n % 10) % 2 == 1) {
                    ans = ans + ((n%10) * (Math.pow(10, pos)));
                }
                n = n / 10;
                pos++;
            }

            long ansL = Math.round(ans);
            
            if (ans > 0) {
                String answer = String.format("oddDigits = %d", ansL);
                System.out.print(answer);
                return ansL;
            }
            else {
                String answer = String.format("oddDigits = -1");
                System.out.print(answer);
                return ansL;
            }
        }
        
        else {
            String answer = String.format("n: %d - Error input!!", n);
            System.out.print(answer); 
            return n; 
        }
    }
}
