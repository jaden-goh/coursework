public class CareerCenterStaff extends User {
    private String staffDepartment;

    public CareerCenterStaff(String id, String name, String passwordHash, String staffDepartment) {
        super(id, name, passwordHash);
        this.staffDepartment = staffDepartment;
    }
    // Getters and setters...
}


