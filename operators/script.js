//All Arithmetic Operators

//addition
let sum = 5+5;
console.log(sum);
//Subtraction 
let sub = 10-3;
console.log(sub);
//multiplication
let res = 5*4;
console.log(res);
//division
let res1 = 10/2;
console.log(res1);
//Modulus
let res2 = 17 % 4;
console.log(res2);
//Exponentiation
let res3 = 2**3;
console.log(res3);

//All assignment operators
//addition assignment
let x = 5;
x +=15;
console.log(x);

let x1 = 10;
x1 = x1+10;
console.log(x1);

//subtraction assignment
let x2 = 5;
x2 -=3;
console.log(x2);

//multiplication assignment
let x3 = 5;
x3 *=6;
console.log(x3);

//division assignment
let x4 = 10;
x4 = x4/2;
console.log(x4);

//modulus assignment
let x5 = 20;
x5 %=6;
console.log(x5);

//exponentiation assignment
let x6 = 4;
x6 = x6**3;
console.log(x6);

//Increment or Decrement Operators
//prefix increment
let xx = 100;
console.log(++xx);
console.log(xx);

//prefix decrement
let yz = 10;
console.log(--yz);
console.log(yz);

//postfix increment
let xy = 200;
console.log(xy++);
console.log(xy);

//postfix decrement
let yx = 20;
console.log(yx--);
console.log(yx);

let _x = 5;
console.log(_x--);
console.log(_x);

//Comparison Operators
let a = 10;
let b = 20;
console.log(a < b);
console.log(a > b);
console.log(a <= b);
console.log(a >= b);
console.log(a == b);
console.log(a != b);
console.log(a !==b);
console.log(a === b);
console.log(a !==b );


let p = '10'
let q = 10
console.log(p==q)
console.log(p===q)
console.log(p!==q)

//logical operators
//logical AND (&&)
let m = 5;
let n = 10;
console.log(m > 0 && n > 0);
console.log(m > 0 && n < 0);
console.log(m < 0 && n > 0);
console.log(m < 0 && n < 0);

//logical OR(||)
let a1 = 5;
let a2 = 10;
console.log(a1 > 0 || a2 > 0);
console.log(a1 > 0 || a2 < 0);
console.log(a1 < 0 || a2 > 0);
console.log(a1 < 0 || a2 < 0);

//logical NOT(!)
let Yes = true;
let No =  false;
console.log(!Yes);
console.log(!No);

//String Operators
console.log("hello" + "World");
console.log("Java" + "Scripts");
console.log("Computer" + "Science");

var lan = "JavaScript";
lan += " Pro";
console.log(lan);

var txt = "Welcome To";
txt += " Programming World";
document.write(txt);

//Operator Precedence
let result = 2+3*4;
console.log(result); 

var result1 = 4+10/5;
console.log(result1);

//operator associativity
//left-to-right associativity
let result2 = 10-5-2;
console.log(result2);

//right-to-left associativity
var result3 = 2**3**2;
console.log(result3);

var result4 = 3**2**3;
console.log(result4);