## 🧱 SOLID Design Principles
# S — Single Responsibility Principle (SRP)

# “For cohesion; avoid making a God Class.”

Each class should have only one reason to change — a single, well-defined purpose.

Keeps classes focused and easy to maintain.

Avoid “God classes” that handle too many responsibilities.

✅ Example:

class InvoiceCalculator { ... }  // handles calculations
class InvoicePrinter { ... }     // handles printing

## O — Open/Closed Principle (OCP)

# “Open for extension, closed for modification.”

You should be able to extend functionality without modifying existing code.

Achieved through abstraction (interfaces, inheritance) or composition.

✅ Example:

interface Shape { void draw(); }

class Circle implements Shape { ... }
class Square implements Shape { ... }


Adding a new Triangle doesn’t require changing existing Shape code.

## L — Liskov Substitution Principle (LSP)

# “Subtypes can replace base types — demand no more, provide no less.”

A subclass should behave as a drop-in replacement for its superclass.

It should not change expected behaviors or assumptions.

❌ Example (violates LSP):

class Bird { void fly(); }
class Penguin extends Bird { void fly() { throw new Error("Can't fly!"); } }


✅ Fix:

interface Bird { }
interface FlyingBird extends Bird { void fly(); }

# # I — Interface Segregation Principle (ISP)

#  Tagline: “Classes should not depend on interfaces they don’t need.”

Break large, general-purpose interfaces into smaller, focused ones.

Prevents “fat interfaces” that force classes to implement unnecessary methods.

✅ Example:

interface Workable { void work(); }
interface Eatable { void eat(); }

class Robot implements Workable { ... }
class Human implements Workable, Eatable { ... }

## D — Dependency Inversion Principle (DIP)

# “Let higher-level modules receive (not create) their lower-level dependencies.”

High-level code should depend on abstractions, not concrete implementations.

Dependencies are injected, not instantiated directly inside the class.

❌ Bad:

class Car {
    private Engine engine = new PetrolEngine();
}


✅ Good:

class Car {
    private Engine engine;
    public Car(Engine engine) { this.engine = engine; } // dependency injection
}


Now you can pass in new ElectricEngine() or mock engines for testing.

