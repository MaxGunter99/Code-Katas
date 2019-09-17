// Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

// solution('abc', 'bc') // returns true
// solution('abc', 'd') // returns false


function solution(str, ending){
    
    // console.log( str.length, ending )
    // console.log( str.length - ending.length )

    let answer = ''

    for ( var i = str.length - ending.length; i < str.length; i++ ) {
        answer = answer + str[i]
    }

    if ( answer === ending ) {
        return true
    } else {
        return false
    }

}

solution('abcde', 'cde') /// returns true
solution('abcde', 'abc') /// returns false

