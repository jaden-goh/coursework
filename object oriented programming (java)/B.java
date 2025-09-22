class B extends A {
    // Override
    @Override
    public void show() {
        System.out.println("B: show()");
    }

    // Overload
    public void greet(int number) {
        System.out.println("B: greet(int) -> " + number);
    }

    // New method (not in A)
    public void onlyInB() {
        System.out.println("B: onlyInB()");
    }
}