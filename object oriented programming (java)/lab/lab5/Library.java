import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


public class Library<T extends Searchable & HasGenre> {
            // a generic can extend one class/interface, the & operator acts
            // another bound that T must have that must be an interface 
            /// (anythign after the & must be interface, extends can be a class)
            
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
    public Set<String> getGenres() {
        Set<String> genres = items.stream()
                                    .map(HasGenre::getGenre)
                                    .collect(Collectors.toSet());

        return genres;    
    }   
    
    public void filter(String genre) {
        List<T> result = items.stream()
                            .filter(item -> item.getGenre().toLowerCase().equals(genre.toLowerCase()))
                            .collect(Collectors.toList());
        result.forEach(item->item.toString());                
    }

    // recommending book with switch
    public void recommendBook(String genre) {
        switch (genre.toLowerCase()) {
            case "fantasy":
            case "romance":
            case "sci-fi":
            case "dystopian":
                filter(genre);
                break;
        default:
            System.out.println("No such genre!");
}};
}
