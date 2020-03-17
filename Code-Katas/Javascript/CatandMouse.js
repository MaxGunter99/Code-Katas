function catMouse(x, j) {

    // If there is a missing animal, return "boring without all three"
    if (x.includes('D') && x.includes('m') && x.includes('C')) {

        // grabs the starting index / ending index Cat -> mouse
        const start = x.indexOf('C');
        const end = x.indexOf('m');
        let count = 0;
        let full = null;

        // if the cat has to jump backwards, reverse the string for the loop so the cat always jumps in the same direction
        if (start < end) {
            full = x.slice(start, end + 1)
        } else {
            full = x.slice(end, start + 1).split('').reverse().join('')
        }

        // If the cat is right next to the mouse and it can jump, it is caught
        if (full.length === 2 && full[1] === 'm' && full.length < j) {
            console.log('Caught!')
            return 'Caught!'
        
        // general check to see if it is possible to catch the mouse
        } else if (full.length - 1 > j) {
            console.log('Escaped!')
            return 'Escaped!'
        }


        // traverses through the full distance
        for (var c = 0; c < full.length; c++) {

            let current = full[c];

            // if the cat cant jump this far, the mouse escapes
            if (count > j) {
                console.log('Escaped')
                return 'Escaped!'

            // if there is a dog in the way, the mouse is protected
            } else if (current === 'D') {
                console.log('Protected!')
                return 'Protected!'

            // if the cat reaches the mouse, it is caught
            } else if (current === 'm') {
                console.log('Caught!')
                return 'Caught!'

            }

            // measuring the distance the cat has jumped
            count++

        }

        // if the cat runs did not jump far enough without a dog in the way, the mouse escapes
        console.log('Escaped')
        return "Escaped!"

    } else {

        console.log("boring without all three")
        return "boring without all three"

    }

}

// catMouse('..D.....Cm', 13) // "Caught!"
// catMouse('............C.............D..m...', 8) // "Escaped!"
// catMouse('m.C...', 5) // "boring without all three"
catMouse('C....mD', 5) // "Caught!"
// catMouse('C.....mD', 5) // "Escaped!"
// catMouse('C..D..m', 5) // 'Protected!'
catMouse('Dm....C', 5) // "Caught!"
// catMouse('Dm.....C', 5) // "Escaped!"
// catMouse('m..D..C', 5) // 'Protected!'




// FROM INTERVIEW
// function catMouse(x, j){

//     if ( x.includes( 'D' ) && x.includes( 'm' ) && x.includes('C') ) {

//       const start = x.indexOf( 'C' );
//       const end = x.indexOf( 'm' )
//       const full = x.slice( start , end + 1 )
//       let map = []
//       let count = 0


//       for ( var c = 0; c < full.length; start > end ? c = c - 1 : c++  ) {

//             let current = full[c];
//             console.log( current )

//             if ( count === j ) {
//               return 'Escaped!'

//             } else if ( current === 'D' ) {
//               return 'Protected!'

//             } else if ( current === 'm' ) {
//               return 'Caught!'

//             }    

//           count = count + 1

//       }

//       return "Escaped!"

//     } else {

//       return "boring without all three"

//     }

// }