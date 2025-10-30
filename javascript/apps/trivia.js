const readline = require('readline');

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let secret_num = getRandomInt(1, 10);

console.log("Bienvenido a Adivina el número");
console.log("El número secreto está entre 1 y 10");

const rl = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
});

let att = 0;

function askQuestion() {
    rl.question("Introduce tu suposición: ", (answer) => {
        let num = parseInt(answer, 10);
        att += 1;

        if (isNaN(num)) {
            console.log("Por favor, introduce un número válido.");
            askQuestion();
            return;
        }

        if (secret_num > num) {
            console.log("El número secreto es mayor");
            askQuestion();
        } else if (secret_num < num) {
            console.log("El número secreto es menor");
            askQuestion();
        } else {
            console.log(`¡Ganaste en ${att} intentos!`);
            rl.close();
        }
    });
}

askQuestion();

