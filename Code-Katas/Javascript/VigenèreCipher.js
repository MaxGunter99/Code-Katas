
function VigenèreCipher( key , abc ) {

    this.encode = function( str ) {

        let answer = []
        let keyCount = 0

        for( var i = 0; i < str.length; i++ ) {

            let newAlphabet = [];
            let character = abc.indexOf( str[ i ] )

            if ( abc.includes( str[ i ] ) ) {

                // creating new instance of alphabet
                for ( var x = 0; x < abc.length; x++  ) {
                    if ( character === abc.length) {
                        character = 0
                    }

                    newAlphabet.push( abc[ character ] )
                    character += 1
                }

                answer.push( newAlphabet[ abc.indexOf( key[ keyCount ] ) ] )

            } else {
                
                answer.push( str[ i ] )

            }
            
            // increment keycount after refferencing the current index
            if ( keyCount === key.length - 1 ) {
                keyCount = 0
            } else {
                keyCount += 1
            }

        }

        console.log( str , '->' , answer.join('') )
        return answer.join('')

    };

    this.decode = function( str ) {

        let answer = [];
        let keyCount = 0

        for ( var i = 0; i < str.length; i++ ) {

            let newAlphabet = [];
            let character = abc.indexOf( key[ keyCount ] )

            if ( abc.includes( str[ i ] ) ) {
                
                for ( var x = 0; x < abc.length; x++  ) {
                    if ( character === abc.length ) {
                        character = 0
                    }
                    newAlphabet.push( abc[ character ] )
                    character += 1
                }

                answer.push( abc[ newAlphabet.join('').indexOf( str[ i ] ) ] )

            } else {
                answer.push( str[ i ] )
            }

            if ( keyCount === key.length - 1 ) {
                keyCount = 0
            } else {
                keyCount += 1
            }
        }

        console.log( 'abc:' , abc )
        console.log( str , '->' , answer.join('') )
        return answer.join('')

    };

}

// var abc , key;
// abc = "abcdefghijklmnopqrstuvwxyz";
// key = "password"
// c = new VigenèreCipher( key , abc );

// c.encode( 'codewars' ) // 'rovwsoiv'
// c.decode( 'rovwsoiv' ) // 'codewars'

// c.encode( 'waffles' ) // 'laxxhsj'
// c.decode( 'laxxhsj' ) // 'waffles'

// c.encode( 'CODEWARS' ) // 'CODEWARS'
// c.decode( 'CODEWARS' ) // 'CODEWARS'

var abc , key;
abc = "abcdefghijklmnopqrstuvwxyz";
key = "pizza"
c = new VigenèreCipher( key , abc );

// c.encode( 'asodavwt' ) // pancakes