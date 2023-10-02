function composition(...fns) {
    return function (value) {
        return fns.reduce((acc, fn) => {
            return fn(acc)
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
    return text.split('').join(' ')
}

const result = composition(
    scream,
    emphasize,
    slowDown
)("para")

console.log(result)