// Given a matrix, unroll the top, then the right then the bottom, then the left, until there is no numbers left.

const sample = [
    [ 10 , 11 , 12 , 13 , 14 ],
    [ 15 , 16 , 17 , 18 , 19 ],
    [ 20 , 21 , 22 , 23 , 24 ],
    [ 25 , 26 , 27 , 28 , 29 ],
    [ 30 , 31 , 32 , 33 , 34 ],
];

const unrolled = []

function Unroll( matrix ) {

    while ( matrix.length > 1 ) {
        remove_top( matrix )
        remove_right( matrix )
        remove_bottom( matrix )
        remove_left( matrix )
        console.log( 'MATRIX:' , matrix )
        console.log( 'UNROLLED:' , unrolled )
    }
}

function remove_top( matrix ) {

    console.log( 'Top:' , unrolled.push( matrix.shift() ) )

}

function remove_right( matrix ) {

    for ( var i = 0; i < matrix.length; i++ ) {
        console.log( "Right:" , unrolled.push( matrix[i].pop() ) )
    }

}

function remove_bottom( matrix ) {

    for ( var i = matrix[ matrix.length -1 ].length - 1; i > -1; i-- ) {
        console.log( 'Bottom:' , unrolled.push( matrix[ matrix.length - 1 ].pop(i) ) )
    }

}

function remove_left( matrix ) {

    for ( var i = matrix.length - 1; i > -1; i-- ) {
        if ( matrix[i].shift() === undefined ) {
            null
        } else {
            console.log( 'Left:' ,  unrolled.push( matrix[i].shift() ) )
        }
    }

}

Unroll( sample )