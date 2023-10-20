// Closure is when a function "remembers" its origin
// Even when executed outside of the file

const sumXPlus3 = require('./closure_scope')
const out = require('./closure_scope')

const x = 1000
console.log(sumXPlus3())

// In this case, the function is using the x defined on the other file
// That is closure


console.log(out())