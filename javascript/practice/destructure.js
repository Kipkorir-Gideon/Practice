const numbers = [1, 2, 3, 4];

[num1, num2]= numbers

const doubleNumbers = numbers.map((num) => {
    return num * 2;
})

console.log(doubleNumbers);
// console.log(num1, num2)

const person = {
    name: 'Gideon',
    age: 29,
    gender: 'male',
    race: 'black'
}

const {name, age} = person;

console.log(name, age);