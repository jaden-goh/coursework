import java.util.*;

public class Shape3DApp {
    public static void main(String[] args) {
        List<Shape3D> shapes = new ArrayList<>();
        shapes.add(new Sphere(10));
        shapes.add(new SquarePyramid(20, 25));
        shapes.add(new Cuboid(50, 20, 30)); // example height = 30

        double totalArea = 0;
        for (Shape3D s : shapes) {
            totalArea += s.area();
        }

        System.out.println("Total surface area of 3D shapes: " + totalArea);
    }
}
