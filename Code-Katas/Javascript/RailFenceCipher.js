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
    


}

// MAXIMUS

// M      M
//  A   I   U
//    X        S

// encodeRailFenceCipher("maximus", 3)
// decodeRailFenceCipher( 'mmaiuxs' , 3 ) // maximus
decodeRailFenceCipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) // "WEAREDISCOVEREDFLEEATONCE"
// encodeRailFenceCipher("WEAREDISCOVEREDFLEEATONCE", 3) // "WECRLTEERDSOEEFEAOCAIVDEN"
// encodeRailFenceCipher("Hello, World!", 3) // "Hoo!el,Wrdl l"