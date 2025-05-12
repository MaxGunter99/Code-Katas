

function sum (numbers) {

    const count = [0]

    for ( var i = 0; i < numbers.length; i++ ) {
        if ( numbers == [] ) {
            return '0'
        } else {
            count.push( numbers[i] + count[ i ] )
        }
    }

    let results = count[ count.length - 1 ]
    console.log( results )
    return results
    
};

sum([]), '0'
sum([1, 5.2, 4, 0, -1]) , '9.2'