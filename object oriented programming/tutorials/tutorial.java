import java.util.Arrays;
import java.util.Scanner;

public class tutorial {
    
    /* Q1: Student -> Object, NTU -> Object, Book -> Class, MichaelJackson -> Object, Age -> Attribute, Color -> Attribute, Work -> Behavior, Person -> Class, Person1 -> Object, Result -> Attribute, Transformer -> Object, Engine -> Attribute, Liquid -> Attribute, Force -> Attribute, Shoot -> Behavior 
    *  Q2: School
            -> Department {name, head of department, courses} 
            -> Courses {course code, difficulty, }
            -> Teacher {PhD, Courses Taught, Office Number, Teacher ID}
            -> Student {major, courses taken, grade level, id}
            -> Rooms {hardware (bool), category (leisure, tutorial, lecture), courses supported}
            
    *   
    */
    // Q3: 
    public static void bubble(int[] a, int n) {
            for (int i = n - 2; i > -1; i -= 1) {
                for (int j = 0; j < i+1; i += 1) {
                    if (a[j] > a[j+1]) {
                        int temp = a[j];
                        a[j] = a[j+1];
                        a[j+1] = temp;
                    }
                }
            }
        }
    
    public static void main (String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number of integer elements to be sorted: ");
        int size = scanner.nextInt();

        int[] a = new int[size];

        for (int i = 0; i < size; i++) {
           
            System.out.printf("Enter integer value for element no. %d", i+1);
            int value = scanner.nextInt();  
            a[i] = value;
        }

        bubble(a,size);

        System.out.println("Final Sorted Array is: ");
        System.out.println(Arrays.toString(a));
        
    }
}