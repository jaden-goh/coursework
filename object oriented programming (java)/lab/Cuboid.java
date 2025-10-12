public class Cuboid implements Shape3D {
    private double length, breadth, height;
    public Cuboid(double length, double breadth, double height) {
        this.length = length;
        this.breadth = breadth;
        this.height = height;
    }
    @Override
    public double area() {
        return 2 * (length * breadth + length * height + breadth * height);
    }
    @Override
    public double volume() {
        return length * breadth * height;
    }
}

