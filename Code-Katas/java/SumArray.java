
public class SumArray {

    /*
    
        Lets create a list of integers that will all be added together and the output will be printed out!
        Lets get familiar with Java <3
    
    */

    public static void main(String[] args) {

        // list of integers, length of 3
        Integer[] list1 = new Integer[ 3 ];
        list1[0] = 5;
        list1[1] = 5;
        list1[2] = 5;

        // easier way
        // Integer[] list2 = { 100, 4, 7, 320 };
        // Integer[] list3 = { 1, 1 };
        // Integer[] list4 = { 0, 0, 0, 0, 0 };
        // Integer[] list5 = {};
        double[] list6 = { 0.5, 5, 24.7 };

        // Integer[] testList = list1;
        // Integer[] testList = list2;
        // Integer[] testList = list3;
        // Integer[] testList = list4;
        // Integer[] testList = list5;
        double[] testList = list6;

        // YOUR CODE HERE ------------

        double total = 0;

        for ( double i: testList ) {
            total = total + i;
        }

        System.out.println( "Total: " + total );
        
    }

}