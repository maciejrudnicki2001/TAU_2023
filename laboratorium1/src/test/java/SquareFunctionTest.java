import static org.junit.Assert.*;

import org.example.SquareFunction;
import org.junit.Test;


public class SquareFunctionTest {

    private SquareFunction squareFunction;

    @Test
    public void checkCalculatingDelta(){
        squareFunction = new SquareFunction(3,5,3);
        int result = squareFunction.calculateDelta();
        assertEquals(-11, result);
    }

    @Test
    public void checkCalculatingDeltaWithNegativeNumbers(){
        squareFunction = new SquareFunction(-3,5,3);
        int result = squareFunction.calculateDelta();
        assertEquals(61, result);
    }

    @Test
    public void checkCalculationHowManyZeroPoints(){
        squareFunction = new SquareFunction(1,5,2);
        int result = squareFunction.calculateHowManyZeroPoints();
        assertEquals(2, result);
    }

    @Test
    public void checkCalculationHowManyZeroPointsButOne(){
        squareFunction = new SquareFunction(3,6,3);
        int result = squareFunction.calculateHowManyZeroPoints();
        assertEquals(1, result);
    }

    @Test
    public void checkCalculationHowManyZeroPointsButZero(){
        squareFunction = new SquareFunction(3,5,3);
        int result = squareFunction.calculateHowManyZeroPoints();
        assertEquals(0, result);
    }

    @Test
    public void checkCalculationValueOfZeroPointsWhenDeltaZero(){
        squareFunction = new SquareFunction(3,6,3);
        double[] result = squareFunction.valueOfZeroNumbers();
        double[] expected = {-1.0};
        assertArrayEquals(expected, result, 0.0001);
    }

    @Test
    public void checkCalculationValueOfZeroPointsWhenDeltaMoreThanZero(){
        squareFunction = new SquareFunction(2,5,3);
        double[] result = squareFunction.valueOfZeroNumbers();
        double[] expected = {-1.5, -1.0};
        assertArrayEquals(expected, result, 0.0001);
    }

}
