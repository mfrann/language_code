//short circuit

// Falso
//false
//0
//null, undefined, NaN, ''

let nombre = 'Martin'
let username = nombre || "Anonimo"

console.log(username)

function fn1(){
    console.log("soy 1")
    return true
}

function fn2(){
    console.log("soy 2")
    return true
}

let x = fn1() && fn2()