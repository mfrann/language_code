const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

async function Calculadora() {
    let a = await askQuestion("Ingresa el primer número: ");
    let b = await askQuestion("Ingresa el segundo número: ");

    // Convertir las entradas a números flotantes
    a = parseFloat(a);
    b = parseFloat(b);

    // Verificar si las entradas son números válidos
    if (isNaN(a) || isNaN(b)) {
        console.log("Por favor, introduce números válidos.");
        rl.close();
        return;
    }

    const operacion = await askQuestion("Elige una operación [ +, -, *, / ]: ").trim();

    let resultado;

    switch (operacion) {
        case "+":
            resultado = a + b;
            break;
        case "-":
            resultado = a - b;
            break;
        case "*":
            resultado = a * b;
            break;
        case "/":
            if (b === 0) {
                console.log("Error: No se puede dividir por cero.");
                rl.close();
                return;
            }
            resultado = a / b;
            break;
        default:
            console.log("Operación no válida. Por favor, elige entre +, -, *, /.");
            rl.close();
            return;
    }

    console.log(`El resultado es: ${resultado}`);
    rl.close();
}

Calculadora();


