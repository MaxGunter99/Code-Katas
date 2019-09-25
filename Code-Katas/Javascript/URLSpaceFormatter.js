// Replace all the spaces from a string to "%20"

function ReplaceSpaces( string ) {

    while ( string.includes( ' ' ) ) {
        string = string.replace( ' ' , '%20' )
        // console.log( answer )
    }

    console.log( `Done: ${string}` )
    return ( string )

};

ReplaceSpaces( 'Hello World My Name Is Max' );