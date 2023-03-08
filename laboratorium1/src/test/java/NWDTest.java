import static org.junit.Assert.*;

import org.example.NWD;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class NWDTest {

    private NWD nwd;

    @Before
    public void setUp(){
        nwd = new NWD();
        System.out.println("Before");
    }

    @After
    public void tearDown(){
        nwd = null;
        System.out.println("After");
    }

    @Test
    public void testNwd() {
        int result = nwd.NWD(4,2);
        assertEquals(2, result);
        System.out.println("Test1");
    }

    @Test
    public void testNwdWhenAisZero(){
        int result = nwd.NWD(4,0);
        assertEquals(4, result);
        System.out.println("Test2");
    }
    @Test
    public void testNwdWhenBisZero(){
        int result = nwd.NWD(0,2);
        assertEquals(2, result);
        System.out.println("Test2");
    }
}
