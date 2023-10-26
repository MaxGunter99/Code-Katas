
// RUN WITH: node RemoveVowels.js

function countVowels( string ) {

    let count = 0
    let vowel_bank = [
        "a", "e", "i", "o", "u", 
        // "A", "E", "I", "O", "U"
    ]

    for ( letter_index in string ) {
        let letter = string[letter_index]
        if ( vowel_bank.includes( letter ) ) {
            count += 1
        } 
    }

    return count

}

countVowels( "hello world" )