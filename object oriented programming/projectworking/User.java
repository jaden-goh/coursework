
public abstract class User {
    protected String id;
    protected String name;
    protected String passwordHash;

    public User(String id, String name, String passwordHash) {
        this.id = id;
        this.name = name;
        this.passwordHash = passwordHash;
    }

    public String getId() { return id; }
    public boolean verifyPassword(String password) { return Hashing.verify(password, passwordHash); }
    public void setPassword(String newPw) { this.passwordHash = Hashing.hash(newPw); }
}

