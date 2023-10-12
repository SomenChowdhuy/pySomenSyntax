//String Data Types
let f_name = "Elon"; //double quotes
let l_name = 'Musk';
console.log(l_name);

let num_0 = 96.0;
console.log(num_0);

var num1 = 100.00;
console.log(num1);

let x = "200";
console.log(typeof x);

let num2 = '1000';
document.write(typeof num2)


let learning = true;
let completed = false;
console.log(learning);
console.log(completed);
console.log(typeof learning);
console.log(typeof completed);


x = 10;
y = 20;
z = y>x;
console.log(z);
console.log(typeof z);


let n = 10>30;
console.log(n);

let n1 = 40<20;
console.log(n1);
console.log(typeof n1);

let n2 = 5>4;
console.log(n2);
console.log(typeof n2);

let age;
console.log(age);

let gender;
console.log(gender);
console.log(typeof gender);

let age1 = 100;
console.log(age1);
console.log(typeof age1);

//Null data type
let y = null;
console.log(y);
console.log(typeof y);
//null is equal to undefined
console.log(null == undefined);

//Reference Data Types empty object
let person = {};
console.log(person);
console.log(typeof person)

//object data dypes key-value pairs
let human = {
    f_name: "Somen",
    l_name: "Chowdhury",
    Age: 30
};
console.log(human);
console.log(typeof human);

//Array Data Types
var num = [10,20,30];
console.log(num);
console.log(typeof num);

//Function Data Types
function display()
{
    console.log("Hey,GreatStack");
}
display();
console.log(typeof display);

//we can store different data types in the same variable
var x1 = "JavaScript";
console.log(x1);
console.log(typeof x1);
x1 = 100.00;
console.log(x1);
console.log(typeof x1);
x1 = true;
console.log(x1);
console.log(typeof x1);
x1 = false;
console.log(x1);
console.log(typeof x1);



var $x = ["Somen",200,true];
console.log($x);