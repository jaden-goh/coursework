public class Sphere implements Shape3D {
    private double radius;
    public Sphere(double radius) {
        this.radius = radius;
    }
    @Override
    public double area() {
        return 4 * Math.PI * radius * radius;
    }
    @Override
    public double volume() {
        return (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);
    }
}
