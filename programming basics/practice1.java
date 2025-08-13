
import java.text.NumberFormat;


public class practice1 {
    
    public static void main(String[] args) {
        
    int principal = 100000;
    float rate = 0.0392F;
    int period = 30;

    int month = period * 12;
    float mortgage = ((float) principal * ((rate)* (float)Math.pow(rate+1, month))/ ((float)Math.pow(rate+1, month) - 1)); 
    String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);

    System.out.println("Mortgage: " + mortgageFormatted);
    
    }

}
