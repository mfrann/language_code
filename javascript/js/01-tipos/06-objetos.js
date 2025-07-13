
//Personaje de TV

let name = "Tony Stark";
let film = "Marvel";
let age = 35;

let player = {
    name: "Tony Stark",    //par llave => valor
    film: "Marvel",
    age: 35,
};

console.log(player);
console.log(player.film);
console.log(player['age']);

//Para eliminar

delete player.age;

console.log(player);
