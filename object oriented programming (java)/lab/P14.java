import java.util.Scanner;

public class P14 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in); 

        System.out.print("Enter your Height: ");
        int height = scanner.nextInt();

        for (int i = 1; i <= height; i++) {
            int j = 0;
            String output = "";
            while (j < i) {
                if (j % 2 == 0) {
                    output = "AA" + output;
                }
                else {
                    output = "BB" + output;
                }
                j += 1;
            }
            System.out.println(output);
        }
    }
}
