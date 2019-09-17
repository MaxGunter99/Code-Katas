
// Given a string, return the string reversed

function reverseLetter(str) {

    let answer = ''

    for ( var i = str.length - 1; i > -1 ; i -- ) {
        if ( str[i] == 'a' || str[i] == 'b' || str[i] == 'c' || str[i] == 'd' || str[i] == 'e' || str[i] == 'f' || str[i] == 'g' || str[i] == 'h' || str[i] == 'i' || str[i] == 'j' || str[i] == 'k' || str[i] == 'l' || str[i] == 'm' || str[i] == 'n' || str[i] == 'o' || str[i] == 'p' || str[i] == 'q' || str[i] == 'r' || str[i] == 's' || str[i] == 't' || str[i] == 'u' || str[i] == 'v' || str[i] == 'w' || str[i] == 'x' || str[i] == 'y' | str[i] == 'z' ) {
            answer = answer + str[i]
        }
    }

    return answer
    
}

reverseLetter("kris9han?."), "nahsirk"