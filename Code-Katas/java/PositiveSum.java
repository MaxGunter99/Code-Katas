import java.util.ArrayList;
import java.util.List;

public class PositiveSum {

    // make a function that will return the sum of any positive number given in an array

    public static void main(String[] args) {
    
        
        List<Integer> testCase = new ArrayList<>();

        // Adds to 15
        // testCase.add( 5 );
        // testCase.add( 4 );
        // testCase.add( 3 );
        // testCase.add( 2 );
        // testCase.add( 1 );
        // testCase.add( -1 );
        // testCase.add( -2 );
        // testCase.add( -3 );
        // testCase.add( -4 );
        // testCase.add( -5 );

        // adds to 0
        // testCase.add( -1 );
        // testCase.add( -1190278 );
        // testCase.add( -97 );
        
        // adds to 1
        testCase.add( 0 );
        testCase.add( 1 );

        int returnedSum = positiveSum( testCase );
        System.out.println( "positiveSum returned: " + returnedSum + "!" );

    }

    public static int positiveSum( List<Integer> numberList ) {

        int sum = 0;

        for ( int i: numberList ) {
            if ( i > 0 ) {
                System.out.println( "Adding: " + i + " to sum" );
                sum += i;

            } else {
                System.out.println( "Skipping: " + i + " (it is negative)" );

            }
        }

        return sum;

    }
    
}
