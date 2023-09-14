// desafio 1

function somar(x) {
    return function(y) {
        return function(z) {
            return x+y+z
        }
    }
}

// console.log(somar(2)(3)(4))

function calc(x) {
    return function(y) {
        return function(fn) {
            return fn(x, y)
        }
    }
}

function sum(a, b) {
    return a + b
}

function times(a, b) {
    return a*b
}

console.log(calc(2)(3)(times))

const carrinho = [
    {nome: 'Caneta', qtde: 10, preco: 7.99, fragil: true},
    {nome: 'Lapis', qtde: 3, preco: 2.99, fragil: false},
    {nome: 'Impressora', qtde: 1, preco: 700.99, fragil: true},
    {nome: 'Borracha', qtde: 1, preco: 10.99, fragil: false},
    {nome: 'Apontador', qtde: 2, preco: 7.9, fragil: true}
]

// const getName = (obj) => obj.nome

// const getTotalPrice = (obj) => obj.qtde * obj.preco

// console.log("map",carrinho.map(getName))
// console.log("map",carrinho.map(getTotalPrice))

// console.log("filter", carrinho.filter((x) => x.preco > 10.00 ))

// desafio 
// 1. fragil true
// 2. qtde * preco -> total
// 3. media dos valores totais
// const count = carrinho.filter((x) => x.fragil).length
// const filter = carrinho.filter((x) => x.fragil).map((x) => x.preco * x.qtde).reduce((x, y) => (x + y) / count) 

// console.log(filter)

// setTimeout(() => {
//     console.log('teste')

//     setTimeout(() => {

//         console.log('teste2')

//         setTimeout(() => {
//             console.log('teste3')
//         }, 2000)
//     }, 2000)
// }, 2000)

function esperarPor(tempo = 2000) {
    return new Promise(function(resolve) {
        setTimeout(() => {
            console.log('executando promise...')
            resolve()
        }, tempo)
    })
}

esperarPor()
    .then(() => esperarPor())
    .then(esperarPor)