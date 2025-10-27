import java.util.ArrayList;
import java.util.List;
import java.util.Set;
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

    public void displayAllItems() {
        this.getAllItems().forEach(item -> item.toString()); 
    }

    // Searching by keyword using streaming
    public void search(String keyword) {
        List<T> result = items.stream()
                    .filter(item -> item.matches(keyword) == true)
                    .collect(Collectors.toList());
        result.forEach(item -> item.toString());
    }
    
    // genres, obtain with stream(), print with lambdas
    public void getGenres() {
        Set<String> genres = items.stream()
                                    .map(Book -> Book.getGenre())
                                    .collect(Collectors.toSet());

        genres.forEach(genre -> System.out.println(genre));
    }   
    
    // recommending book with switch
    public static void recommendBook() {};
}
