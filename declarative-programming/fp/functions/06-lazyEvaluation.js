function eager(a, b) {
    // heavy process

    const end = Date.now() + 2500
    while (Date.now() < end) {}

    const value = Math.pow(a, 3)
    return value + b
}

function lazy(a) {
    // heavy process

    const end = Date.now() + 2500
    while (Date.now() < end) {}

    const value = Math.pow(a, 3)
    return function (b) {
        return value + b
    }
}

console.time("#1")
console.log(eager(3, 100))
console.log(eager(3, 200))
console.log(eager(3, 300))
console.timeEnd("#1")

console.time("#2")
const lazyHelper = lazy(3)
console.log(lazyHelper(100))
console.log(lazyHelper(200))
console.log(lazyHelper(300))
console.timeEnd("#2")

// on the second case, the lazy function uses the lexic context of the previus functions executions
// so it only has to execute the function inside the function, not everything like on case #1
