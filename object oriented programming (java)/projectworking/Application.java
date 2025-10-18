public class Application {
    private String id, studentId, internshipId;
    private LocalDateTime submittedAt;
    private ApplicationStatus status;
    private boolean placementConfirmed, withdrawalRequested;

    public Application(String id, String studentId, String internshipId) {
        this.id = id;
        this.studentId = studentId;
        this.internshipId = internshipId;
        this.submittedAt = LocalDateTime.now();
        this.status = ApplicationStatus.PENDING;
        this.placementConfirmed = false;
    }
    // Getters and setters...
}
