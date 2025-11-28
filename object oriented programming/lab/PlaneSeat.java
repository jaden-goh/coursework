public class PlaneSeat {
    private int seatId;
    private boolean assigned;
    private int customerId = -1;

    public PlaneSeat(int seatID) {
        this.seatId = seatID;
    }
        
    public int getSeatID() {
        return seatId;
    }

    public int getCustomerID() {
        return customerId;
    }

    public boolean isOccupied() { 
        return assigned;
    }

    public void assign(int customerId) {
        this.customerId = customerId;
        this.assigned = true;
    }

    public void unAssign() {
        this.customerId = -1;
    }
}
