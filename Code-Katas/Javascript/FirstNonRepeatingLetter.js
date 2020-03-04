// Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.
// For example, if given the input 'stress', the function should return 't', 
// since the letter t only occurs once in the string, and occurs first in the string.
// if there are no single letters return ''

function firstNonRepeatingLetter(s) {
    
    lowerCaseS = s.toLowerCase()

    for ( x in lowerCaseS ) {

        let before = lowerCaseS.substring( 0 , x )
        let after = lowerCaseS.substring( Number( x ) + 1 )
        let section = before + after

        if ( section.includes( lowerCaseS[x] ) ) {
            null
        } else {

            console.log( s[x] )
            return s[x]

        }

    }

    return ''

}

// firstNonRepeatingLetter('stress') // t
firstNonRepeatingLetter( 'aa' ) // a
firstNonRepeatingLetter( 'abba' ) // a
// firstNonRepeatingLetter('zaaaaaaaaaaa') // z
// firstNonRepeatingLetter( 'moonmen' ) // e