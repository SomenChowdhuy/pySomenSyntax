//var variable
var f_name = "shutterstock";
var l_Name = "adobestock";
console.log(f_name);
console.log(l_Name);

//let variable
let x1 = 10;
if(x1>5){
    let x2 = 100;
    console.log(x2);
} 
console.log(x2);

//const variable
const x = 10;
console.log(x);
x = 30;


//global scope
var _x = "Welcome,buddies";
function display(){
    console.log(_x);
}
display();
console.log(_x);


//Block Scope
function display(){
    if(true){
        let str = "Ireen Ara";
        console.log(str);
    }
}
display();
console.log(str);

//function scope
function display(){
    var fs = "Ladies & Gentleman";
    console.log(fs);
}
display();
console.log(fs);