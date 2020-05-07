
// Using Regex, seperate the numbers out from a string.

returnNumbers = ( string , solution ) => {

    let answer = string.replace( /([a-zA-Z])/g , '' )

    { answer === solution ? console.log( 'Pass:' , answer ) : console.log( 'Fail:' , answer ) }

}

returnNumbers( '' , '' )
returnNumbers( 'aBc' , '' )
returnNumbers( '123abc' , '123')
returnNumbers( '123abc456' , '123456')
returnNumbers( '1aA2bBb3sklajlak093874nk2j3nkj5b3kf98sd8f23n4289y' , '1230938742353988234289')