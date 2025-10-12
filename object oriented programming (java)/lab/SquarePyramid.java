public class SquarePyramid implements Shape3D {
    private double baseLength, height;
    public SquarePyramid(double baseLength, double height) {
        this.baseLength = baseLength;
        this.height = height;
    }
    @Override
    public double area() {
        double slantHeight = Math.sqrt((baseLength/2)*(baseLength/2) + height*height);
        return baseLength * baseLength + 2 * baseLength * slantHeight;
    }
    @Override
    public double volume() {
        return (1.0/3.0) * baseLength * baseLength * height;
    }
}
