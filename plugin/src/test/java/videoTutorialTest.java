import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class videoTutorialTest {
    @Test
    public void TestNormalNumbers() {
        videoTutorial x = new videoTutorial();
        Assertions.assertEquals("1", x.convert(1));
        Assertions.assertEquals("2", x.convert(2));
    }
    @Test
    public void testThreeNumbers() {
        videoTutorial x = new videoTutorial();
        Assertions.assertEquals("Newman", x.convert(3));
    }
    @Test
    public void testFiveNumbers() {
        videoTutorial x = new videoTutorial();
        Assertions.assertEquals("Rosie", x.convert(5));
    }
    @Test
    public void testThirteenNumbers() {
        videoTutorial x = new videoTutorial();
        Assertions.assertEquals("Kramer", x.convert(13));
    }
}
