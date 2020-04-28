function positiveSum(arr) {
    var count = 0;

    for ( x in arr ) {
        let current = arr[x]
        current > 0 ? count += current : null
    }

    return count
}

// positiveSum([]) // 0
// positiveSum([1,2,3,4,5]) // 15
// positiveSum([1,-2,3,4,5]) // 13
// positiveSum([-1,-2,-3,-4,-5]) // 0
// positiveSum([-1,2,3,4,-5]) // 9