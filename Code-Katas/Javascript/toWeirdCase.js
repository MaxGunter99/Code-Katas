
// Write a function toWeirdCase that accepts a string, 
// and returns the same string with all even indexed characters in each word upper cased, 
// and all odd indexed characters in each word lower cased. 
// The indexing just explained is zero based, so the zero-ith index is even, 
// therefore that character should be upper cased.

function toWeirdCase(string){

    let answer = string.split(' ');
    let formatted = [];
    for (words in answer) {

        let word = answer[words];

        for ( letter in word ) {

            if ( letter % 2 === 0 ) {
                formatted.push( word[letter].toUpperCase())
            } else {
                formatted.push( word[letter] )
            }

        }

        if ( words < answer.length - 1 ) {
            formatted.push( ' ' )
        }

    }

    console.log( formatted.join('') )
    return formatted.join('')

}

// toWeirdCase('is') // 'Is'
toWeirdCase('This is a test') // 'ThIs Is A TeSt'