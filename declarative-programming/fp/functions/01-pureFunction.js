// A pure function is a function where the return value is determined by the parameters, with no side effects

const pi = 3.14

// impure
function circArea(r) {
    return r*r*pi
}

//pure
function circArea2(r, pi) {
    return r*r*pi
}

console.log(circArea(10))


// to be considered pure function, there can not be any value or const declared outside the function
// Using pure functions is always good and should be prioritized if possible
// a function that generates random Number, is also considered impure function
// its also good for tests, so no mock is needed
// its important to have consistency on the function's return, to be considered pure