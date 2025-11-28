public class Zoo {
    interface Flyable {
        void fly();
    }
     
    interface Swimmable {
        void swim();
    }

    abstract class Animal {
        protected String name;
        protected int age;

        public Animal(String n, int a) {
            name = n;
            age = a;
        }

        abstract void speak();

        public void eat() {
            System.out.println(this.name + " is eating...");
        }

        public void eat(String food) {
            System.out.println(this.name + " is eating " + food);
        }   
    }

    public class Dog extends Animal implements Swimmable {
        public Dog(String name, int age) {
            super(name, age);
        }

        public void swim() {
            System.out.println(name + " is Swimming...");
        }

        public void speak() {
            System.out.println("Woof!");
        }
    }

    public class Bird extends Animal implements Flyable {
        public Bird(String name, int age) {
            super(name, age);
        }

        public void fly() {
            System.out.println(name + " is Flying...");
        }

        public void speak() {
            System.out.println("Tweet!");
        }
    }
    
    public class Duck extends Animal implements Swimmable, Flyable {
        public Duck(String name, int age) {
            super(name, age);
        }

        public void fly() {
            System.out.println(name + " is Flying...");
        }

        public void swim() {
            System.out.println(name + " is Swimming...");
        }

        public void speak() {
            System.out.println("Quack!");
        }
    }

    Animal dog = new Dog("Buddy", 5);
    Animal bird = new Bird("Tweety", 2);
    Animal duck = new Duck("Donals", 3);
    
    // Error from here, illegal start of type ???
    dog.speak();
    dog.eat();
    dog.eat("bone");   // method overloading
    ((Swimmable) dog).swim();

    bird.speak();
    bird.eat("seeds");
    ((Flyable) bird).fly();

    duck.speak();
    duck.eat();
    ((Flyable) duck).fly();
    ((Swimmable) duck).swim();

    public static void main(String[] args) {
        Zoo myZoo = new Zoo();
        }
    }
