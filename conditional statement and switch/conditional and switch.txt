// Conditional Statements
//if
if(true){
    console.log("I love her");
}

if(false){
    console.log("I dislike her"); 
}

let age = 20;
if(age>18){
    console.log("You are an adult and eligible for casting vote");
}

let age1 = 16;
if(age1>18){
    console.log("You are an adult");
}

let country = "Bangladesh";
let age2 = 20;
if(age2 >= 18 && country == "Bangladesh"){
    document.write("You can get a driver's licesnce");
}

let country1 = "Bangladesh";
let age3 = 20;
if(age3 >= 18 && country1 == "India"){
    document.write("You can get a driver's licesnce");
}

//if...else
let age4 = 16;
if(age4 > 18){
    console.log("You are an adult");
}
else{
    console.log("You are a minor");
}

let age5 = 15;
if(age5 >= 18){
    console.log("You are an adult");
}
else if(age5 >= 16){
    console.log("You are a teenager");
}
else{
    console.log("You are a minor");
}

// Switch
let value = 42;
switch(typeof value){
    case "number":
        console.log("Number");
        break;
    case "string":
        console.log("String");
        break;
    case "boolean":
        console.log("Boolean");
        break;
    default:
        console.log("Other");
        break;
}


let val = "somen";
switch(typeof val){
    case "number":
        console.log("Number");
        break;
    case  "string":
        console.log("String");
        break;
    case "boolean":
        console.log("Bool");
        break;
    default:
        break;
}


let val1 = true;
switch(typeof val1){
    case "number":
        console.log("Number");
        break;
    case "string":
        console.log("String");
        break;
    case "boolean":
        console.log("bool");
        break;
    default:
        break;
}


let val2 = [];
switch(typeof val2){
    case "number":
        console.log("Number");
        break;
    case "string":
        console.log("String");
        break;
    case "boolean":
        console.log("bool");
        break;
    default:
        console.log("Other");
        break;
}




let dayName = 3;
switch(dayName){
    case 1:
        dayName = "Sunday";
        break;
    case 2:
        dayName = "Monday";
        break;
    case 3:
        dayName = "Tuesday";
        break;
    case 4:
        dayName = "Wednesday";
        break;
    case 5:
        dayName = "Thursday";
        break;
    case 6:
        dayName = "Friday"
        break;
    default:
        dayName = "Invalid day number";
        break;
}
console.log("The day is: "+dayName);



var day = 2;
switch(day){
    case 1:
        day = "Saturday";
        break;
    case 2:
        day = "Sunday";
        break;
    case 3:
        day= "Monday";
        break;
    default:
        day = "invalid";
        break;
}
document.getElementById("demo").innerHTML = "Today is "+day;




//ternary operator
//condition? val_if_true : val_if_false
let age6 = 20;
let msg = (age >=18)? "you are an adult": "you are a minor";
console.log(msg);

let age7 = 16;
let msg1 = (age7 >=18)? "you are an adult" : "you are a minor";
console.log(msg1); 



