
// Write a function that checks if a string is a permutation of another. ex: "Levo" , "Love"

public class Permutations {

    public static void main(String[] args) throws Exception {

        TestCase[] tests = {
            new TestCase( 
                "Love", 
                "veLo", 
                true 
            ),
            new TestCase( 
                "", 
                "", 
                true 
            ),
            new TestCase( 
                "abc", 
                "xyz", 
                false 
            ),
            new TestCase( 
                "Destiny", 
                "ynitseD", 
                true 
            ),
            new TestCase( 
                "Hello World", 
                "dlrow olleh", 
                true 
            ),
        };

        int testId = 1;

        for ( TestCase test: tests ) {
            
            boolean functionResponse = checkPermutations( test.permutation(), test.givenString() );
            System.out.println();

            if ( functionResponse != test.givenStringIsPermutation() ) {

                System.out.println( "Test (" + testId + ") --- FAILED" );
                System.out.println( "Permutation: " + test.permutation() );
                System.out.println( "Given String: " + test.givenString() );
                throw new Exception(
                    "\n\n Function checkPermutations returned: "
                    + functionResponse 
                    + " , should equal: "
                    + test.givenStringIsPermutation()
                    + "\n\n"
                );

            }

            System.out.println( "Test (" + testId + ") --- PASSED" );
            testId++;

        }

        
    }

    public static boolean checkPermutations( String permutation, String givenString ) {

        boolean isPermutation = true;

        // ... logic
        String lowerCasePermutation = permutation.toLowerCase();
        String lowerCaseGivenString = givenString.toLowerCase();

        String letterBank = lowerCasePermutation;
        
        for ( char i: lowerCaseGivenString.toCharArray() ) {
            String letter = Character.toString( i );
            boolean letterInBank = letterBank.contains( letter );

            // System.out.println( "letterBank: " + letterBank );
            // System.out.println( "letter: " + letter );

            if ( letterInBank ) {
                letterBank = letterBank.replaceFirst(letter, "");

            } else {
                System.out.println( "Letter: " + letter + " is not in the letterBank:" + letterBank );
                isPermutation = false;
                break;
            }

        }

        return isPermutation;

    }
    
}

// USING CLASS TO STORE TEST CASE DATA
// class TestCase {
    
//     String permutation;
//     String givenString;
//     Boolean givenStringIsPermutation;

//     public TestCase( String permutation, String givenString, boolean givenStringIsPermutation ) {
//         this.permutation = permutation;
//         this.givenString = givenString;
//         this.givenStringIsPermutation = givenStringIsPermutation;
//     }
    
// }
    
// USING RECORD TO STORE TEST CASE DATA ( requires java 17 )
record TestCase( String permutation, String givenString, boolean givenStringIsPermutation ){}