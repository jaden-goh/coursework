public class Student extends User {
    private int year;
    private String major;
    private String acceptedPlacementId;

    public Student(String id, String name, String passwordHash, int year, String major) {
        super(id, name, passwordHash);
        this.year = year;
        this.major = major;
    }
    // Getters and setters...
}

