function decipherThis(str , solution) {

    let splitString = str.split( ' ' )
    let answer = []

    for ( x in splitString ) {

        let current = splitString[x];
        let numbers = current.split(/([^\d])/)[0];
        let letters = current.replace( numbers , '' );

        if ( letters.length > 1 && numbers !== '' ) {

            var one = letters[0]
            var two = letters[ letters.length - 1 ]
            temp = letters.split('')
            temp[0] = two
            temp[ temp.length - 1 ] = one
            letters = temp.join('')

        }

        { numbers !== '' ? decodedWord = String.fromCharCode( numbers ) + letters : decodedWord = letters }
        answer.push( decodedWord )

    }

    console.log( 'Yours:' , answer.join( ' ' ) )
    console.log( 'Right:' , solution )
    { answer.join(' ') === solution ? console.log( 'Pass' ) : console.log( 'Fail' ) }
    return answer.join( ' ' )

}; 

// decipherThis('72eva 97 103o 97t 116sih 97dn 115ee 104wo 121uo 100o' , 'Have a go at this and see how you do' )
decipherThis( '78gnyefy 106zzjyjm 117ettnft 118slcvzf 101nsnfin' , 'Nynyefg jmzjyjz utttnfe vflcvzs ensnfin' )