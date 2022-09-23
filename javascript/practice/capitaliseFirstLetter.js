var name = prompt("Enter your name: ");

var firstChar = name.slice(0, 1);

var capitaliseFirstChar = firstChar.toUpperCase();

var restOfChar = name.slice(1, name.length);
restOfChar = restOfChar.toLowerCase();

var capitaliseName = capitaliseFirstChar + restOfChar;

alert("Hello, " + capitaliseName);