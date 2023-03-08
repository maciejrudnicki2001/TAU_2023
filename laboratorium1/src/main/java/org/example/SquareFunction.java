package org.example;

public class SquareFunction {

    private final int a,b,c;

    public SquareFunction(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }


    public int calculateDelta() {
        return b * b - 4 * a * c;
    }

    public int calculateHowManyZeroPoints() {
        int delta = calculateDelta();

        if (delta < 0) {
            return 0;
        } else if (delta == 0){
            return 1;
        } else {
            return 2;
        }
    }

    public double[] valueOfZeroNumbers() {
        int zeroPoints = calculateHowManyZeroPoints();
        if(zeroPoints == 0){
            return new double[]{};
        } else if ( zeroPoints == 1) {
            double x = -b / (2.0 * a);
            return new double[]{x};
        } else {
            double x1 = (-b - Math.sqrt(calculateDelta())) / (2.0 * a);
            double x2 = (-b + Math.sqrt(calculateDelta())) / (2.0 * a);
            return new double[]{x1, x2};
        }
    }
}
