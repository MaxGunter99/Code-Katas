
public class ReverseString {

    public static void main(String[] args) {
        
        String testString = "Hello";

        StringBuilder reverseString = new StringBuilder();

        for ( int i = testString.length() - 1; i >= 0; i-- ) {
            char letter = testString.charAt( i );
            reverseString.append( letter );
        }
        
        System.out.println( "Test String: " + testString );
        System.out.println( "Reverse String: " + reverseString );

    }

}