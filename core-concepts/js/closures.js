

// JS closures limit where you can reference variables

// Global variables / top level variables are defined like this and the function can reference myTestVar
var myTestVar = "Hello"

function printMyTestVar() {
  console.log( myTestVar )
}

printMyTestVar()

// However, variables use closures to limit where it can be referenced. This would throw an undefined error

// function printMyTestVar() {
//   var myTestVar = "Hello"
// }
// console.log( myTestVar )

// printMyTestVar()