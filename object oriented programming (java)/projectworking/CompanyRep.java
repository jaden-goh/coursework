
public class CompanyRep extends User {
    private String companyName, department, position;
    private boolean isApproved;

    public CompanyRep(String id, String name, String passwordHash, String companyName, String department, String position, boolean isApproved) {
        super(id, name, passwordHash);
        this.companyName = companyName;
        this.department = department;
        this.position = position;
        this.isApproved = isApproved;
    }
    // Getters and setters...
}


