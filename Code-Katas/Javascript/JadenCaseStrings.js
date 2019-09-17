// Jaden Casing Strings

// Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
// Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

String.prototype.toJadenCase = function () {

    let word = []

    for ( var i = 0; i < str.length; i++ ) {
        
        if ( str[i] === ' ' ) {

            word.push(' ')

        }  else if (  word[ word.length -1 ] === ' ' ) {

            word.push( str[ i ].toUpperCase() )

        } else {

            word.push( str[i] )

        }

    }

    // console.log( word.join().replace(/,/g, '') )
    return( word.join().replace(/,/g, '') )
};

var str = "How can mirrors be real if our eyes aren't real";
str.toJadenCase()