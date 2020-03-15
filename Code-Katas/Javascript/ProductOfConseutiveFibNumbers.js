// go through the fib process and if 2 consecutive numbers = the number given to the function, return them as true

function productFib(prod) {

    let fib = [0, 1, 1]

    while( fib.length ) {

        let multiplied = fib[fib.length - 2] * fib[fib.length - 1]

        if ( multiplied >= prod ) {

            if ( multiplied == prod ) {

                let answer = [  fib[fib.length - 2] , fib[fib.length - 1] , true ]
                console.log( answer )
                return answer

            } else {

                let answer = [  fib[fib.length - 2] , fib[fib.length - 1] , false ]
                console.log( answer )
                return answer

            }

        } else {

            let next = fib[fib.length - 2] + fib[fib.length - 1]
            fib.push(next)

        }
    }
}

productFib(4895) // [55, 89, true]
productFib(5895) // [89, 144, false]
productFib(74049690) // [6765, 10946, true]
productFib(84049690) // [10946, 17711, false]
productFib(193864606) // [10946, 17711, true]
productFib(447577) // [610, 987, false]
productFib(602070) // [610, 987, true]