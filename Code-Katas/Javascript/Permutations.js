// Write a function that checks if a string is a permutation of another. ex: "Levo" , "Love"

function CheckPermutations( x , y ) {

    console.log( x , y )

    check = []

    for ( var i = 0; i < y.length; i++ ) {

        if ( x.includes( y[i] ) ) {
            check.push( 'yes' )

        } else {
            check.push( 'no' )

        }
    }

    console.log( check )
    if ( check.includes( 'no' ) ) {
        console.log( 'Not a permutation' )
    } else {
        console.log( 'Is a permutation' )
    }
}

CheckPermutations( "Love" , "oveLx" )