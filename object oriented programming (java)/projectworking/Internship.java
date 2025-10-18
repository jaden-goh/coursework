
public class Internship {
    private String id, title, description, level, preferredMajor, companyName, repId;
    private LocalDate openDate, closeDate;
    private InternshipStatus status;
    private int slots;
    private boolean visible;

    public boolean isOpenFor(Student s) {
        return visible && status == InternshipStatus.APPROVED && !LocalDate.now().isBefore(openDate) && !LocalDate.now().isAfter(closeDate);
    }
    public boolean hasVacancy() { return slots > 0; }
    // Getters and setters...
}