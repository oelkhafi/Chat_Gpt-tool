public class videoTutorial {
    public static void main(String[] args) {
        for(int x = 1; x <= 100; x++) {
            System.out.println(convert(x));
        }
    }
    public static String convert(int input) {
        if(input % 3 == 0 ) {
            return "Newman";
        }
        if(input % 5 == 0 ) {
            return "Rosie";
        }
        if(input % 13 == 0 ) {
            return "Kramer";
        }
        return String.valueOf(input);
    }
}
