// Using Regex, return the numbers from a string.

returnLetters = ( string , solution ) => {

    let answer = string.replace( /([0-9])/g , '' )

    { answer === solution ? console.log( 'Pass:' , answer ) : console.log( 'Fail:' , answer ) }

}

returnLetters( '' , '')
returnLetters( '123' , '')
returnLetters( '123abc' , 'abc')
returnLetters( '123aBc456' , 'aBc')
returnLetters( '1aA2bBb3sklajlak093874nk2j3nkj5b3kf98sd8f23n4289y' , 'aAbBbsklajlaknkjnkjbkfsdfny')