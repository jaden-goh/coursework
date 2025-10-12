public class SalePerson implements Comparable<SalePerson> {
    private String firstName;
    private String lastName;
    private int totalSales;

    public SalePerson(String firstName, String lastName, int totalSales) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.totalSales = totalSales;
    }

    @Override
    public String toString() {
        String out = this.firstName + ", " + this.lastName + ": " + this.totalSales;
        return out; 
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true  ;
        if (o == null || getClass() != o.getClass()) return false;

        SalePerson other = (SalePerson) o;
        return firstName.equals(other.firstName) &&
            lastName.equals(other.lastName);
    }

    @Override
    public int compareTo(SalePerson other) {
    if (this.totalSales != other.totalSales) {
        return Integer.compare(other.totalSales, this.totalSales);
    }
    return this.lastName.compareTo(other.lastName);
    }

    public String getFirstName() {
        return this.firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public int getTotalSales() {
        return this.totalSales;
    }

}
