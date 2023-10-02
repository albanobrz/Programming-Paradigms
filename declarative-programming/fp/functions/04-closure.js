// closure is when a function "remembers" its origin,
// even when executed outside of the file

const sumXPlus3 = require('./closure_scope')
const out = require('./closure_scope')

const x = 1000
console.log(sumXPlus3())

// in this case, the function is using the x defined on the other file
// that is closure


console.log(out())