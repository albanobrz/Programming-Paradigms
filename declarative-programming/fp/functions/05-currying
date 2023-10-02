// currying is a base and important comcept on the functional programming
// it's basically calling a function inside another function

function sum(a) {
    return function (b) {
        return function (c) {
            return a + b + c
        }
    }
}

console.log(sum(1)(2)(3))

// this way of declaring a function, gives a lot of flexibility
// another exemple

// Another exemple with no currying
function textWithLengthBetween(min, max, err, text) {
    const length = (text || '').trim().length

    if (length < min || length > max) {
        throw err
    }
}

const p1 = {nome: "A", price: 14.00, desc: 0.2}
textWithLengthBetween(4, 255, "invalid name", p1.nome)

// with currying

function textWithLengthBetween(min, max, err, text) {
    return function (max) {
        return function(err) {
            return function(text) {
                const length = (text || '').trim().length
            
                if (length < min || length > max) {
                    throw err
                }
            }
        }
    }
}

textWithLengthBetween(4)(255)("invalid name")(p1.nome)

// even better, reusing the functions

function applyValidation(fn) {
    return function (value) {
        try {
            fn(value)
        } catch(e) {
            return {error: e}
        }
    }
}

const forceRightLength = textWithLengthBetween(4)(255)
const forceValidProductName = forceRightLength("Invalid name")
const validateProductName = applyValidation(forceValidProductName)

const p2 = {nome: "AB", price: 11.00, desc: 0.3}

console.log(validateProductName(p2.nome))
