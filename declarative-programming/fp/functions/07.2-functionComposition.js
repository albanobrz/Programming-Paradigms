// This file is a copy from the 07 file.

// This function was modified to accept async functions
function composition(...fns) {
    return function (value) {
        return fns.reduce(async (acc, fn) => {
            if (Promise.resolve(acc) === acc) {
                return fn(await acc)
            } else {
                return fn(acc)
            }
        }, value)
    }
}

function scream(text) {
    return text.toUpperCase()
}

function emphasize(text) {
    return `${text}!!!!!!`
}

function slowDown(text) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(text.split('').join(' '))
        }, 3000)
    })
}

const result = composition(
    scream,
    emphasize,
    slowDown
)("para")

const exagerated = composition(
    scream,
    emphasize,
    slowDown
)

exagerated("pare").then(console.log())

console.log(result)