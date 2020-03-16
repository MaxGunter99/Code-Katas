
const dict = {
    1: 'I',
    5: 'V',
    50: 'L',
    10: 'X',
    100: 'C',
    500: 'D',
    1000: 'M',
}

const RomanNumerals = {

    toRoman(x) {

        // If the number is in the dictionary, return it
        if ( dict[x] ) {

            console.log( 'In dictionary:' , dict[x] )
            return dict[x]

        } else {

            let eq = []

            for ( var i = 0; i < String(x).length; i++ ) {

                let current = String(x)[i]
                let place = ''
                let count = Number( String(x).length - i - 1 )
                
                for ( var placement = 0; placement < count; placement++ ) {
                    place += '0'
                }

                if ( place !== 0 ) {
                    if ( Number( String(x)[i] + place ) > 1000 ) {

                        for ( var p = 0; p < Number( String(x)[i] + place ) / 1000; p++ ) {
                            eq.push( 1000 )
                        }

                    } else if ( Number( String(x)[i] ) !== 0 ) {
                        if ( Number( String(x)[i] ) === 8 ) {
                            eq.push( 5 )
                            eq.push( 3 )
                        } else {

                            eq.push( String(x)[i] + place )
                        }
                    }

                } else {
                    eq.push( Number( String(x)[i] ) )
                }
            }

            let answer = []

            for ( i in eq ) {

                let current = eq[i]
                // console.log( current )

                if ( dict[current] ) {
                    answer.push( dict[current] )

                } else if ( Number( current ) === 3 ) {
                    answer.push( 'III' )

                } else {

                    let abort = false

                    for ( x in dict ){
                        for ( y in dict ) {

                            if ( !abort ) {

                                if ( Number( x ) +  Number( y ) === Number( current ) ) {
                                    // console.log( dict[x] + dict[y] )
                                    answer.push( dict[y] , dict[x] )
                                    abort = true
        
                                } else if ( Number( x ) -  Number( y ) === Number( current ) ) {
                                    // console.log( dict[y] + dict[x] )
                                    answer.push( dict[y] , dict[x] )
                                    abort = true
        
                                } 
                            }
                        }
                    }

                }

            }

            console.log( 'Answer:' , answer.join('') )
            return answer.join('')

        }


    },

    fromRoman(x) {

        let split = x.split('')

        // console.log( split )
        for ( i in split ) {

            let index = Object.values(dict).indexOf( split[i] )
            split[i] = Object.keys( dict )[index]

        }

        let sum = 0;

        for ( var y = 0; y < split.length; y++ ) {

            if ( y >= split.length - 2 || split.length === 2 ) {

                if ( split[y] < split[y + 1] ) {
                    number = Number( split[y + 1] ) - Number( split[y] )
                    sum = sum + Number( number )
                    y = split.length

                } else {
                    sum = sum + Number( split[y] )
                }

            } else {
                sum = sum + Number( split[y] )

            }
        }

        console.log( 'Answer:' , sum )
        return sum
    }
}

RomanNumerals.toRoman(1) // 'I'
RomanNumerals.toRoman(3) // 'III'
RomanNumerals.toRoman(4) // 'IV'
RomanNumerals.toRoman(13) // 'XIII'
RomanNumerals.toRoman(1000) // 'M'
RomanNumerals.toRoman(999) // "CMXCIX"
RomanNumerals.toRoman(1991) // 'MCMXCI'
RomanNumerals.toRoman(2006) // 'MMVI'
RomanNumerals.toRoman(2004) // 'MMIV'
RomanNumerals.toRoman(2008) // 'MMVIII'
RomanNumerals.toRoman(2020) // 'MMXX'

RomanNumerals.fromRoman('I') // 1
RomanNumerals.fromRoman('III') // 3
RomanNumerals.fromRoman('IV') // 4
RomanNumerals.fromRoman('XIII') // 13
RomanNumerals.fromRoman('XIV') // 14
RomanNumerals.fromRoman('XXI') // 21
RomanNumerals.fromRoman('MMIV') // 2007
RomanNumerals.fromRoman('MMVII') // 2007
RomanNumerals.fromRoman('MMVIII') // 2008
RomanNumerals.fromRoman('MDCLXIX') // 1669