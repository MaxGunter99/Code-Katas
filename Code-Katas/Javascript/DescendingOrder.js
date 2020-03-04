// Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. 
//Essentially, rearrange the digits to create the highest possible number.

function descendingOrder(n) {

    let arr = n.toString().split('');
    const answer = [];

    while (arr.length) {

        let index = 0;

        for (var i = 0; i < arr.length; i++) {

            if (index === i) {
                i = i++
            } else {

                if (arr[index] < arr[i]) {

                    index = i

                } else if (arr[index] == arr[i]) {

                    arr.splice(index, index - 1)
                    index = 0
                    break

                }

            }
        }

        answer.push(arr[index])
        arr.splice(arr.indexOf(arr[index]), 1);

    }

    const finalAnswer = answer.join('')
    console.log(finalAnswer)
    return Number(finalAnswer)

}

// descendingOrder(0) // 0
// descendingOrder(1) // 1
descendingOrder(123456789) // 987654321
// descendingOrder(1021) // 2110