import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


public class Library<T extends Searchable> {
    private List<T> items;

    public Library() {
        this.items = new ArrayList<>();
    }

    public void addItem(T item) {
        items.add(item);
        System.out.println("Added: " + item.toString());
    }

    public boolean removeItem(T item) {
        if (items.remove(item)) {
            System.out.println("Removed: " + item.toString());
            return true;
        }
        System.out.println("Item not found: " + item.toString());
        return false;
    }

    public List<T> getAllItems() {
        return new ArrayList<>(items); 
    }

    public List<T> search(String keyword) {
        return items.stream()
                    .filter(item -> item.matches(keyword))
                    .collect(Collectors.toList());
    }
    
    
}
