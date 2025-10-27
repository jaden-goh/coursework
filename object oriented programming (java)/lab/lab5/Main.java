import java.util.*;

public class Main {
    public class LibraryApp {
        public static void main(String args[]) {
            Library<Book> Lib1 = new Library<>();

            List<Book> books = Arrays.asList(
            new Book("1984", "George Orwell", "Dystopian", 1949),
            new Book("The Hobbit", "J.R.R. Tolkien", "Fantasy",1937),
            new Book("Pride and Prejudice", "Jane Austen", "Romance", 1813) 
            );
            
            // add too lib1, with lambda
            books.forEach(book -> Lib1.addItem(book));
        
            
        }

        public static void recommendBook() {};
    }               
}

