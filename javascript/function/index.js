function myBMI(weight, height) {
    return Math.floor(weight / (height * height));
}

var bmi = myBMI(65, 1.8)
console.log(bmi)