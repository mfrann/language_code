class Person {
  name: string;
  age: number;
  active: boolean;

  constructor(name: string, age: number, active: boolean) {
    this.name = name;
    this.age = age;
    this.active = active;
  }
}

function readPerson(person) {
  console.log(person);
}

const myUsers = [
  ["Martin", 18, true],
  ["Jose", 29, false],
  ["Alex", 34, true],
];

readPerson(myUsers[2]);

//PASS

function getFirst(list) {
  console.log(list[0]);
}

const myLIist = ["Perro", "Gato", "Conejo"];
getFirst(myLIist);
