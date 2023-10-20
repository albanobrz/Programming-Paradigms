// First class function means that the programming language treats the function as a variable
// So its possible to store functions inside variables

const x = 3
const y = function(txt) {
    return `this is the text ${txt}`
}

const z = () => console.log('Arrow :)')

console.log(x)
console.log(y("Hi"))
z()

// A language is only possible to be considered functional, if it has first class functions and higher order functions