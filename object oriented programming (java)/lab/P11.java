import java.util.Scanner;

public class P11 {
    public static void main(String[] args) {
        System.out.print("Enter a Character:");
        Scanner scanner = new Scanner(System.in); // scanner is your variable where it takes in an input such as in Python: name = input("Enter your name: ") 
        String input = scanner.next().toLowerCase();

        switch (input) {
            case "a":
                System.out.println("Action movie fan\n");
                break;
            case "c":
                System.out.println("Comedy movie fan\n");
                break;
            case "d":
                System.out.println("Drama movie fan\n");
                break;
            default:
                System.out.println("Invalid choice\n");
                break;

        }

    }
}
