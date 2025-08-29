import java.util.Scanner;

public class P12 {
    public static void  main(String args[]) {
        
        Scanner scanner = new Scanner(System.in); 

        System.out.print("Enter your Salary: \n");
        int salary = scanner.nextInt();

        System.out.print("Enter your Merit Points: \n");
        int merit = scanner.nextInt();

        if (salary < 600) {
            String grade = "C";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }
        
        if (salary >= 600 && salary < 649 && merit < 10) {
            String grade = "C";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }
        
        if (salary >= 600 && salary < 649 && merit >= 10) {
            String grade = "B";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }

        if (salary >= 650 && salary < 700) {
            String grade = "B";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }
        
        if (salary >= 700 && salary < 799 && merit < 20) {
            String grade = "B";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }
        
        if (salary >= 700 && salary < 799 && merit >= 20) {
            String grade = "A";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }

        if (salary >= 799) {
            String grade = "A";
            System.out.println("salary : " + salary + ", merit : " + merit + " - Grade " + grade);
        }

    }
}