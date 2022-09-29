// function myBMI(weight, height) {
//     return Math.floor(weight / (height * height));
// }

// var bmi = myBMI(65, 1.8)
// console.log(bmi)


// var loveScore = Math.random() * 100;
// loveScore = Math.floor(loveScore) + 1;

// if (loveScore > 70) {
//     var message = "Your love score is " + loveScore + "%, You love each other like Kanye loves Kanye.";
//     console.log(message);
// }
// else {
//     console.log(loveScore);
// }




// function isLeap(year) {
//     if (year % 4 == 0 && year % 400 == 0) {
//         console.log("It is a leap year");
//     }

//     else if (year % 4 == 0 && year % 100 == 0) {
//         console.log("It is not a leap year");
//     }
//     else {
//         console.log("It is not a leap year");
//     }
// }

// isLeap(2100)


// var names = ["Mark", "Milicent", "Bob", "Grace", "Naomy", "George", "ELizabeth", "Tony"]

// console.log(names.includes("Mark"))

// for (num = 1; num < 101; num++) {
//     if (num % 3 === 0 && num % 5 === 0) {
//         console.log("FizzBuzz");
//     }
//     else if (num % 3 === 0) {
//         console.log("Fizz");
//     }
//     else if (num % 5 === 0) {
//         console.log("Buzz");
//     }
//     else {
//         console.log(num);
//     }
// }

// var output = [];
// function fizzBuzz() {
//     for (var num = 1; num < 101; num++) {
//         if (num % 3 === 0 && num % 5 === 0) {
//             output.push("FizzBuzz");
//         }
//         else if (num % 3 === 0) {
//             output.push("Fizz");
//         }
//         else if (num % 5 === 0) {
//             output.push("Buzz");
//         }
//         else {
//             output.push(num)
//         }
//     }

//     console.log(output);
// }

// fizzBuzz()



// function whosPaying(names) {
//     var numberOfPeople = names.length;
//     var randomPersonPosition = Math.floor(Math.random() * numberOfPeople);
//     var randomPerson = names[randomPersonPosition];

//     console.log(randomPerson + " is going to buy lunch today.");
 
// }

// whosPaying(["Arnold", "Paul", "Cecilia", "Phylis", "Fred", "Mona"])

// var count = 99
// function bottlesOfBeer() {
//     while (count > 0) {
//         console.log(count + " bottles of beer on the wall, " + count + " bottles of beer.")
    
//         count--;
//         console.log("Take one down and pass it around, " + count + " bottles of beer on the wall.")
//     }
    
// }

// bottlesOfBeer()
// console.log("No more bottles of beer on the wall, no more bottles of beer.")
// console.log("Go to the store and buy some more, " + count + " bottles of beer on the wall.")



function fibonacciGenerator(n) {
    var output = [];
    if (n === 1) {
        output = [0];
    }
    else if (n === 2) {
        output = [0, 1];
    }
    else {
        output = [0, 1];
        for (var i = 2; i < n; i++) {
            output.push(output[output.length - 2] + output[output.length - 1]);
        }
    }
    return output;
}

output = fibonacciGenerator(6)
console.log(output);