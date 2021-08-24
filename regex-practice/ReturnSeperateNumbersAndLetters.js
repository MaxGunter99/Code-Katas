
// Using Regex, seperate the numbers from letters.
// ex: Seperate( '123abc456' , [ '123456' , 'abc' ] )

Seperate = ( string , solution ) => {

    const ref = string;
    let numbers = ref.replace( /([a-zA-Z])/g , '' );
    let letters = ref.replace( /([0-9])/g , '' )
    let answer = { numbers , letters }
    { answer = solution ? console.log( 'Pass:' , answer ) : console.log( 'Fail:' , answer ) }

}

Seperate( '' , { numbers: '' , letters: '' } )
Seperate( 'aBc' , { numbers: '' , letters: 'aBc' } )
Seperate( '123abc' , { numbers: '123' , letters: 'abc' } )
Seperate( '123abc456' , { numbers: '123456' , letters: 'abc' } )
Seperate( '1aA2bBb3sklajlak093874nk2j3nkj5b3kf98sd8f23n4289y' , { numbers: '1230938742353988234289' , letters: 'aAbBbsklajlaknkjnkjbkfsdfny' } )