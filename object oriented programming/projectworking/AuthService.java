import java.util.*;

public class AuthService {
    private UserRegistry userRegistry;

    public User login(String id, String password) {
        User u = userRegistry.findById(id);
        if (u != null && u.verifyPassword(password)) return u;
        throw new RuntimeException("Invalid credentials");
    }

    public void changePassword(User u, String newPassword) {
        u.setPassword(newPassword);
    }
}