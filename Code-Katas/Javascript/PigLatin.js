// Return a string in pig latin

function pigIt(str){
    
    let split = str.split(' ');
    let answer = [];

    for ( x in split ) {

        let latin = split[x];

        if ( latin === '!' || latin === '?' || latin === '.' ) {
            answer.push( latin[0] )
        } else {
            answer.push( latin.slice(1) + latin[0] + 'ay' )
        }

    }

    console.log( answer.join(' ') )
    return answer.join(' ')

}

// pigIt('Pig latin is cool') //'igPay atinlay siay oolcay'
pigIt( 'Hello world !' )