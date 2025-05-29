

public class RemoveVowels {
    
    public static void main(String[] args) throws Exception {

        String[][] tests = {
            { "x", "x" },
            { "a", "" },
            { "aeiou", "" },
            { "A", "" },
            { "AEIOU", "" },
            { "Hey", "Hy" },
            { "Hello World", "Hll Wrld" },
            { "23452345234#^&&%^___+~~~", "23452345234#^&&%^___+~~~" },
        };
        int testNumber = 0;

        for ( String[] testCase: tests ) {

            testNumber++;

            String test = testCase[0];
            String testSolution = testCase[1];

            String mySolution = (String)removeVowelsFromString( test );
            String testStatus = mySolution.equals( testSolution ) ? "PASS" : "FAIL";

            System.out.println( "----- Test (" + testNumber + "): " + testStatus );
            
            if ( testStatus == "FAIL" ) {
                System.out.println( "Test String: " + test );
                throw new Exception( "\n\n Your Solution: " + mySolution + " != Expected solution: " + testSolution + "\n" );
            }

        }


    }

    public static String removeVowelsFromString( String testString ) {

        // String[] vowelBank = { 
        //     "a", "e", "i", "o", "u" 
        // };
        String vowelBank = "aeiouAEIOU";

        StringBuilder solution = new StringBuilder();

        for ( 
            char letter: testString.toCharArray()
        ) {

            if ( vowelBank.indexOf( letter ) == -1 ) {
                solution.append( letter );
            }
        }

        return solution.toString();
    }

}
