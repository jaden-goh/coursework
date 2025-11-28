class Circle {
        private double radius; // radius
        private static final double pi = 3.14159;

        public Circle(double rad) {
            this.radius = rad;
        
        }
        
        public void setRadius(double rad) {
            this.radius = rad;
        }
        
        public double getRadius() {
            return this.radius;
        }

        public double area() {
            double area = Circle.pi * this.radius * this.radius;
            return area;
        }

        public double circumference() {
            double circ = Circle.pi * (2*this.radius);
            return circ;
        }

        public void printArea() {
            double area = this.area();
            System.out.println(area);
        }
        public void printCircumference() {
            double circ = this.circumference();
            System.out.println(circ);
        }
    }

class Dice {
        private int valueOfDice;

        public Dice(int val) {
            this.valueOfDice = val;
        }
        
        public void setDiceValue(int val) {
            this.valueOfDice = (int)(Math.random()*6) + 1;
        }

        public int getDiceValue(int val) {
            return this.valueOfDice;
        }

        public void printDiceValue() {
            int val = this.valueOfDice;
            System.out.println(val);
        }
    }

public class tutorial2 {
    
    
}


