public class TestPolymorphism {
    public static void main(String[] args) {
        A a = new A();       // plain parent
        B b = new B();       // plain child
        A upcast = new B();  // upcast child -> parent ref

        // Case 1: method exists in A, overridden in B
        a.show();       // A: show()
        b.show();       // B: show()
        upcast.show();  // B: show()   <-- runtime polymorphism

        // Case 2: method exists in A, NOT overridden in B
        upcast.greet("Hello");  // A: greet(String)

        // Case 3: overload only exists in B
        // b.greet(5);          // works
        // upcast.greet(5);     // compile error (A doesn't know greet(int))

        // Case 4: method exists only in B
        // b.onlyInB();         // works
        // upcast.onlyInB();    // compile error
    }
}