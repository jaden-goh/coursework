import java.util.Scanner;

public class PlaneApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Plane plane = new Plane();  // your Plane class

        int choice;
        do {
            System.out.println("\n==== Plane Seat Reservation System ====");
            System.out.println("(1) Show number of empty seats");
            System.out.println("(2) Show list of empty seats");
            System.out.println("(3) Show list of seat assignments by Seat ID");
            System.out.println("(4) Show list of seat assignments by Customer ID");
            System.out.println("(5) Assign a customer to a seat");
            System.out.println("(6) Remove a seat assignment");
            System.out.println("(7) Quit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    plane.showNumEmptySeats();
                    break;
                case 2:
                    plane.showEmptySeats();
                    break;
                case 3:
                    plane.showAssignedSeats(true);
                    break;
                case 4:
                    plane.showAssignedSeats(false);
                    break;
                case 5:
                    System.out.print("Enter seat ID: ");
                    int seatId = sc.nextInt();
                    System.out.print("Enter customer ID: ");
                    int custId = sc.nextInt();
                    plane.assignSeat(seatId, custId);
                    break;
                case 6:
                    System.out.print("Enter seat ID to unassign: ");
                    int seatToRemove = sc.nextInt();
                    plane.unAssignSeat(seatToRemove);
                    break;
                case 7:
                    System.out.println("Program terminating…");
                    break;
                default:
                    System.out.println("Invalid choice, please try again.");
            }
        } while (choice != 7);
    }
}
