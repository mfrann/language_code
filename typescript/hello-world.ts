/* === COMENTARIO === */
// ---- DE UNA LINEA ----

console.log("Hola, TypeScript");

/* === VARIABLES === */

var myName = "Martin";
console.log(myName);

var myString: string = "Caycho";
//myString = 5; -> DA ERROR

myString = "Falcon";

console.log(myString);
console.log(typeof myString);

/*VARIABLE NUMBER*/

let myNumber: number = 7;
myNumber = myNumber + 4;
console.log(myNumber);
console.log(typeof myNumber);

let myNumber2 = 4.5;
console.log(myNumber2);
console.log(typeof myNumber2);

/* === VARIABLE BOOLEAN === */

let myBool: boolean = false;
console.log(myBool);
console.log(typeof myBool);

let myUndefined: undefined;
//myUndefined = "myUndefined" --> ERROR
console.log(myUndefined);

/* === CONSTANTES === */
const myConst = "Mi constante";
//myConst = "Otro valor" --> ERROR
console.log(myConst);

/* === CONTROLES DE FLUJO === */

myNumber = 10;
myString = "Adios";

if (myNumber === 10 && myString === "Hola") {
  console.log("El valor es 10");
} else if (myNumber === 11 || myString === "Hola") {
  console.log("El valor es 11");
} else {
  console.log("No es ni 10 ni 11");
}

/* === FUNCIONES  ===*/

function myFuction(): string {
  return "Mi funcion";
}

console.log(myFuction());

function sumNumbers(a: number, b: number): number {
  return a + b;
}

console.log(sumNumbers(10, 20));

/* === LISTAS ===*/
let myList: Array<string> = ["Martin", "Caycho", "18"];
console.log(myList);

let mySet: Set<string> = new Set(["Martin", "Caycho", "Martin", "18"]);
mySet.add("@mfrann");
console.log(mySet);

let myMap: Map<string, number> = new Map([
  ["Martin", 36],
  ["Caycho", 20],
  ["Martin", 18],
]);

myMap.set("Kylex", 29);
console.log(myMap);

/* === BUCLES ===*/

for (const value of myList) {
  console.log(value);
}

let myCounter = 0;

while (myCounter < myList.length) {
  console.log(myList[myCounter]);
  myCounter++;
}

/* === CLASES ===*/

class MyClass {
  name: string;
  age: number;
  height: number;
  favColor: string;

  constructor(name: string, age: number, height: number, favColor: string) {
    this.name = name;
    this.age = age;
    this.height = height;
    this.favColor = favColor;
  }
}

let myClass = new MyClass("Martin", 18, 1.65, "Cian");
console.log(myClass);
console.log(myClass.name);

/* === ENUM ===*/

/*
const enum MyEnum {
  DART = "dart",
  PYTHON = "python",
  SWIFT = "swift",
  JAVA = "java",
  KOTLIN = "kotlin",
  JAVASCRIPT = "javascript",
}

const myEnum = MyEnum.DART;
console.log(myEnum);
*/
