public class EvenOrOdd {
    
    public static void main(String[] args) {
        
        // Integer myNumber = 1;
        // Integer myNumber = 10;
        Integer myNumber = 3;

        Integer evenOrOdd = myNumber % 2;

        String solution;
        if ( evenOrOdd == 0 ) {
            solution = "Even";
        } else {
            solution = "Odd";
        }

        System.out.println( myNumber + " is " + solution );

    }

}
