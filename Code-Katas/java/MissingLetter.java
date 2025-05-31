
// Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

// You will always get an valid array. And it will be always exactly one letter be missing. 
// The length of the array will always be at least 3.
// The array will always contain letters in only one case.

// Example:
// ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

public class MissingLetter {
    
    public static void main(String[] args) throws Exception {
        
        String[][] tests = {
            { "acd", "b" },
            { "bce", "d" },
            { "efh", "g" } ,
            { "abd", "c" },
            { "wyz", "x" },
        };

        for ( String[] testCase: tests ) {

            String test = testCase[0];
            String solution = testCase[1];

            System.out.println( "Testing: " + test );
            String returnedLetter = findMissingAlphabetLetter( test );
            System.out.println( "Returned: " + returnedLetter );
            
            if ( !solution.equals( returnedLetter ) ) {
                System.out.println( "Status: FAIL" );
                throw new Exception( "\n\n Expected: " + solution + " but got: " + returnedLetter + "\n" );
            }

            System.out.println( "Status: PASS" );
            System.out.println();

        }


        
    }

    public static String findMissingAlphabetLetter( String givenString ) {

        String missingLetter = null;

        String alphabet = "abcdefghijklmnopqrstuvwxyz";

        // get starting index from given string
        char startLetter = givenString.charAt( 0 );
        int startIndex = alphabet.indexOf( startLetter );
        char endLetter = givenString.charAt( givenString.length() - 1 );
        int endIndex = alphabet.indexOf( endLetter ) + 1;

        int currentIndex = 0;

        for ( int i = startIndex; i < endIndex; i++ ) {

            String alphabetSlice = alphabet.substring( i, i + 1 );
            String givenStringSlice = givenString.substring( currentIndex, currentIndex + 1 );
            Boolean slicesMatch = alphabetSlice.equals( givenStringSlice );

            // System.out.println( alphabetSlice + " --- " + givenStringSlice );
            // System.out.println( "Slice Matches: " + slicesMatch );

            if ( !slicesMatch ) {
                missingLetter = alphabet.substring( i, i + 1 );
                break;
            }

            currentIndex++;

        }

        return missingLetter;

    }



}
