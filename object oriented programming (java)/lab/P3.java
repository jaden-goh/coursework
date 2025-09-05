import java.util.Scanner;

public class P3 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in); 

        System.out.print("Enter your Starting Value: \n");
        int starting = scanner.nextInt();

        System.out.print("Enter the Ending Value: \n");
        int ending = scanner.nextInt();

        System.out.print("Enter the Incremental Value: \n");
        int increment = scanner.nextInt();

        int starting1 = starting;
        int ending1 = ending;

        int starting2 = starting;
        int ending2 = ending;

        if (ending < starting || ((ending-starting)%increment) != 0 ) {
            System.out.println("Error Input.");
        }
        else {
            System.out.println("US$      S$");
            System.out.println("--------------");
            for (int i = starting; i <= ending; i += increment) {
                System.out.println(i+"      "+(1.82*i)); 
            }
        

        System.out.println("US$      S$");
        System.out.println("--------------");
        while (starting1 <= ending1) {
            System.out.println(starting1+"      "+(1.82*starting1));
            starting1 += increment;
        }


        System.out.println("US$      S$");
        System.out.println("--------------");
        do {
            System.out.println(starting2+"      "+(1.82*starting2));
            starting2 += increment;
        } while (starting2 <= ending2);

        }
    }
}
