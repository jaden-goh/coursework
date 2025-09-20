public class Plane {
    private PlaneSeat [] seat = new PlaneSeat[12];
    private int numEmptySeat = 12;

    public Plane() {
    this.numEmptySeat = 12;  // all seats empty at the start
    for (int i = 0; i < seat.length; i++) {
        seat[i] = new PlaneSeat(i + 1);  // seat IDs from 1 to 12
    }
}

    private PlaneSeat[] sortSeats() {
    PlaneSeat[] temp = seat.clone();  // clone to avoid modifying original
    int n = temp.length;
    boolean swapped;

    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (temp[j] != null && temp[j + 1] != null && 
                temp[j].getCustomerID() > temp[j + 1].getCustomerID()) {

                // swap PlaneSeat objects
                PlaneSeat t = temp[j];
                temp[j] = temp[j + 1];
                temp[j + 1] = t;
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted
    }

        return temp; }
    
    public void showNumEmptySeats() {
        System.out.printf("There are %d empty seats.", numEmptySeat);
    }

    public void showEmptySeats() {
        System.out.println("List of Unoccupied Seats:");
        for (int i = 0; i < this.seat.length; i++) {
            if (seat[i].isOccupied() == false) {
                System.out.println(seat[i].getSeatID());
            }
        }
        System.out.println("===========================");
    }

    public void showAssignedSeats(boolean bySeatId) {
        if (bySeatId == false) {
            PlaneSeat[] sorted = this.sortSeats();
            for (int i = 0; i < sorted.length; i++) {
                System.out.printf("Seat ID: %d, Customer ID: %d", sorted[i].getSeatID(), sorted[i].getCustomerID());
            }
        }

        if (bySeatId == true) {
            for (int i = 0; i < seat.length; i++) {
                System.out.printf("Seat ID: %d, Customer ID: %d", seat[i].getSeatID(), seat[i].getCustomerID());
            }
        }
    }

    public void assignSeat(int seatID, int custId) {
        for (int i = 0; i < seat.length; i++) {
            if (seat[i].getSeatID() == seatID) { 
                if (seat[i].isOccupied() == false) {
                    seat[i].assign(custId);
                    this.numEmptySeat -= 1;
                    break;
                }
                
                else {
                    System.out.println("Seat is Occupied!");
                }
            }
        }
    }

    public void unAssignSeat(int seatID) {
        for (int i = 0; i < seat.length; i++) {
            if (seat[i].getSeatID() == seatID) { 
                if (seat[i].isOccupied() == true) {
                    seat[i].unAssign();
                    break;
                }
                
                else {
                    System.out.println("Seat is already unoccupied!");
                }
            }
        }
    }
}