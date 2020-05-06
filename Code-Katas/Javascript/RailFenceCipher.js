// UNFINISHED

// "WEAREDISCOVEREDFLEEATONCE"

// W       E       C       R       L       T       E
//   E   R   D   S   O   E   E   F   E   A   O   C  
//     A       I       V       D       E       N  

// WECRLTEERDSOEEFEAOCAIVDEN ( no spaces in that, purely demonstational )

function encodeRailFenceCipher(string, numberRails) {

    const structure = [];
    let rail = 0;
    let direction = 'down'

    for ( var x = 0; x < numberRails; x++) {
        structure.push( [] )
    }

    for ( var i = 0; i < string.length; i++ ) {
        structure[ rail ].push( string[ i ] )
        if ( direction === 'down' ) {
            if ( rail === numberRails - 2 ) {
                direction = 'up'
            }
            rail += 1
        } else if ( direction === 'up' ) {
            if ( rail === 1 ) {
                direction = 'down'
            }
            rail -= 1
        }
    }

    let answer = []

    for ( i in structure ) {
        answer.push( structure[i].join('') )
    }

    console.log( structure , answer.join('') )
    return answer.join('')

}

// W       E       C       R       L       T       E
//--------------------------------------------------
//   E   R   D   S   O   E   E   F   E   A   O   C  
//--------------------------------------------------
//     A       I       V       D       E       N 
  
function decodeRailFenceCipher(string, numberRails) {

    let rail = numberRails
    let decoded = []

    for ( var x = 0; x < numberRails; x++) {
        decoded.push( [] )
        for ( i in string ) {
            decoded[ x ].push( '' )
        }
    }

    for ( var i = 0; i < decoded.length; i++ ) {

        for ( var x = i; x < string.length; x += rail ) {
            decoded[ i ][x] = []
        }
        rail -= 1
        
    }

    

    console.log( decoded )
    return decoded.join('')

}

// MAXIMUS

// M      M
//  A   I   U
//    X        S

decodeRailFenceCipher( 'mmaiuxs' , 3 ) // maximus
// decodeRailFenceCipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) // "WEAREDISCOVEREDFLEEATONCE"
// decodeRailFenceCipher( 'WECRLTEERDSOEEFEAOCAIVDEN' , 5 ) // WLSADOOTEEECEAEECRFINVEDR
// decodeRailFenceCipher( 'WIREEEDSEEEACAECVDLTNROFO', 4 ) // 'WEAREDISCOVEREDFLEEATONCE'

// encodeRailFenceCipher("maximus", 3)
// encodeRailFenceCipher("WEAREDISCOVEREDFLEEATONCE", 3) // "WECRLTEERDSOEEFEAOCAIVDEN"
// encodeRailFenceCipher("Hello, World!", 3) // "Hoo!el,Wrdl l"