// class Greeter {
//     greeting: string

//     constructor(message: string) {
//         this.greeting = message
//     }
//     greet(): string {
//         return this.greeting
//     }
// }

// let greeter = new Greeter('Hello world!')
// console.log(greeter.greet())

// let myFavoritePet: 'dog';
// myFavoritePet = 'dog'

// type Species = 'cat' | 'dog' | 'bird'

// interface Pet {
//     species: Species;
//     name: string;
//     eat(): string;
//     walk(): string;
//     sleep(): string;
// }

// interface Cat extends Pet {
//     species: 'cat'
// }

// interface Dog extends Pet {
//     species: 'dog'
// }

// interface Bird extends Pet {
//     species: 'bird'
//     sing(): string
// }


// function buyPet(pet: Species, name: string): Pet {
//     if (pet === 'cat') {
//         return {
//             species: 'cat',
//             name: name,
//             eat: function () {
//                 console.log(`${this.name} eats.`)
//             },
//             walk: function () {
//                 console.log(`${this.name} walks.`)
//             },
//             sleep: function () {
//                 console.log(`${this.name} sleeps.`)
//             }
//         } as Cat
//     } else if (pet === 'dog') {
//         return {
//             species: 'dog',
//             name: name,
//             eat: function () {
//                 console.log(`${this.name} eats.`)
//             },
//             walk: function () {
//                 console.log(`${this.name} walks.`)
//             },
//             sleep: function () {
//                 console.log(`${this.name} sleeps.`)
//             }
//         } as Dog
//     } else if (pet === 'bird') {
//         return {
//             species: 'bird',
//             name: name,
//             eat: function () {
//                 console.log(`${this.name} eats.`)
//             },
//             walk: function () {
//                 console.log(`${this.name} walks.`)
//             },
//             sleep: function () {
//                 console.log(`${this.name} sleeps.`)
//             },
//             sing: function () {
//                 console.log(`${this.name} sings.`)
//             }
//         } as Bird
//     } else {
//         throw `Sorry we do not have a ${pet}. Would you like to buy a dog?`
//     }
// }

// function petIsCat(pet: Pet): pet is Cat {
//     return pet.species === 'cat'
// }

// function petIsDog(pet: Pet): pet is Dog {
//     return pet.species === 'dog'
// }

// function petIsBird(pet: Pet): pet is Bird {
//     return pet.species === 'bird'
// }

// function playWithPet(pet: Pet) {
//     console.log(`Hey ${pet.name}, lets play.`)

//     if (petIsCat(pet)) {
//         pet.eat()
//         pet.sleep()
//     } else if (petIsDog(pet)) {
//         pet.eat()
//         pet.walk()
//         pet.sleep()
//     } else if (petIsBird(pet)) {
//         pet.eat()
//         pet.sing()
//         pet.sleep()
//     } else {
//         throw 'An unknown pet. Did you buy a rock?'
//     }
// }

// let dog = buyPet(myFavoritePet, 'Rocky')

// playWithPet(dog)


// let threePigs: number[] = [1, 2, 3]

// console.log(threePigs)

// let genericStringArray: Array<string> = ['first', 'second', 'third']

// console.log(genericStringArray)

// enum Day { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday }

// let bestDay: Day = Day.Saturday

// console.log(bestDay)

// enum tenPlus { Ten = 10, Eleven, Twelve }

// console.log(tenPlus.Twelve)


// function log(): void {
//     console.log('I return nothing')
// }

// log()



// interface Fruit {
//     name: string
//     quantity: number
// }

// const inventory: Fruit[] = [
//     { name: 'apples', quantity: 2 },
//     { name: 'bananas', quantity: 0 },
//     { name: 'cherries', quantity: 5 }
// ]

// const findCherries = (fruit: Fruit): boolean => {
//     return fruit.name === 'cherries';
// }

// const cherries = inventory.find(findCherries)

// console.log(cherries)

// const apples = inventory.find((e: Fruit) => e.name === 'apples')

// console.log(apples)


enum SomeEnum { A, B }

let enumValues: Array<string> = []

for (let value in SomeEnum) {
    if(typeof SomeEnum[value] === 'number') {
        enumValues.push(value)
    }
}

enumValues.forEach(v => console.log(v))
