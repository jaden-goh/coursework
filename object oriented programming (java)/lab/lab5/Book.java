
public class Book implements Searchable, HasGenre {
    public String title;
    public String author;
    public String genre;
    public int publicationYear;

    public Book(String title, String author, String genre, int publicationYear) {
        this.title = title.toLowerCase();
        this.author = author.toLowerCase();
        this.genre = genre.toLowerCase();
        this.publicationYear = publicationYear;
    }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    @Override
    public String getGenre() { return genre; }
    public int getPublicationYear() { return publicationYear; }

    @Override
    public boolean matches(String keyword) {
        keyword = keyword.toLowerCase();
        return title.toLowerCase().contains(keyword);
    }

    @Override
    public String toString() {
        return String.format("%s by %s [%s]", title, author, genre);
    }


}
