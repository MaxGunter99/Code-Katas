
public class toWeirdCase {

    public static void main(String[] args) throws Exception {
        
        String[][] testCases = {
            { "Hello World", "HeLlO WoRlD" },
            { "Max", "MaX" },
            { "max", "MaX" },
            { "Lil Nas X", "LiL NaS X" },
            { "happy pride month", "HaPpY PrIdE MoNtH" },
        };

        int testNumber = 1;

        for ( String[] testCase: testCases ) {

            String test = testCase[0];
            String testSolution = testCase[1];

            String weirdCase = (String)stringToWeirdCase( test );

            if ( !testSolution.equals( weirdCase ) ) {
                System.out.println( "Test " + testNumber + " FAIL" );
                throw new Exception( "\n\n stringToWeirdCase returned: " + weirdCase + " -- Should equal: " + testSolution + "\n\n"  );
            }

            System.out.println( "Test " + testNumber + " PASS" );
            testNumber++;

        }

    }

    public static String stringToWeirdCase( String myString ) {

        int index = 0;
        boolean charIsUpper = true;

        StringBuilder mySolution = new StringBuilder();

        for( char i: myString.toCharArray() ) {

            char letter = myString.charAt( index );
            // System.out.println( letter );

            if ( myString.charAt(index) == ' ' ) {
                mySolution.append(" ");
                index++;
                charIsUpper = true;
                continue;
            }

            if ( charIsUpper ) {
                mySolution.append( Character.toUpperCase(letter) );
            } else {
                mySolution.append( Character.toLowerCase(letter) );
            }

            index++;
            charIsUpper = !charIsUpper;
        }
    
        return mySolution.toString();
    
    }
}

