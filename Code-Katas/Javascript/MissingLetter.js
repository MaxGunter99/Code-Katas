// Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

// You will always get an valid array. And it will be always exactly one letter be missing. 
// The length of the array will always be at least 2.
// The array will always contain letters in only one case.

// Example:
// ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

function findMissingLetter(array) {

    let arr = array.join('').toLowerCase();
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let beginning = alphabet.indexOf( array[0].toLowerCase() );
    let end = alphabet.indexOf( array[ array.length - 1 ].toLowerCase() ) + 1;

    let slice = alphabet.slice( beginning , end );
    console.log( slice , arr )

    for ( i in slice ) {

        if ( arr.includes( slice[i] ) ) {
            null
        } else {

            if ( array[0] === array[0].toLowerCase() ) {

                console.log( slice[i].toLowerCase() )
                return slice[i].toLowerCase() 

            } else {

                console.log( slice[i].toUpperCase() )
                return slice[i].toUpperCase() 

            }
        }

    }

}

// findMissingLetter(['a','b','c','d','f']) //'e'
findMissingLetter(['O','Q','R','S']) //'P'