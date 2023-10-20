// Functor is an object that implements the map function 
// Tt is a "wrapper" of a value 

const nums = [1, 2, 3, 4, 5, 6]

const newNums = nums
    .map(x => x + 10)
    .map(x => x * 2)

console.log(nums, newNums)

// Array is an exemple of functor

function SecureType(value) {
    return {
        value: value,
        invalid() {
            return this.value === null || this.value === undefined
        },
        map(fn) {
            if (this.invalid()) {
                return SecureType(null) 
            } else {
                const newValue = fn(this.value)
                return SecureType(newValue)
            }
        }
    }
}

const firstText = "this is a text"
const result = SecureType(firstText)
    .map(t => t.toUpperCase())
    .map(t => `${t}!!!!`)
    .map(t => t.split('').join(' '))

console.log(firstText, result.value)

// Tts basically a method that execute a chain of functions