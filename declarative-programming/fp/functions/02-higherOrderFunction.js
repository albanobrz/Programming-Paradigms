// A higher order function is basically, pass a function as argument to another function or returning a function from a function
// Not all programming languages support this feature
// That means that not all languages has the functional paradigm

function execute(fn, ...params) {
    return fn(...params)
}

function sum(a, b, c) {
    return a + b + c
}

function multiply(a, b) {
    return a * b
}

const r1 = execute(sum, 4, 5, 6)
const r2 = execute(multiply, 2, 2)

console.log(r1, r2)