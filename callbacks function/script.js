//exercise 1
//callback function
function sample(a,b,cb){
    var c = a+b;
    var d = a-b;
    var res = cb(c,d);
    return res;
}

function sum(a,b){
    return a + b;
}

var res = sample(5,8,sum);
console.log(res);

var res1 = sample(4,3,function(c,d){ 
    // console.log(c,d);
    return c-d;
})
console.log(res1);

var res2 = sample(5,8,function(c,d){
    return c*d;
})
console.log(res2);


//exercise 2
//Anonymous funciton
// (i)
var sum = function(x,y){
    return x+y;
}
console.log(sum(10,30));

//(ii)
( 
function(){
    console.log("Welcome To GreatStack");
}
)();

//(iii)
setTimeout(function(){
    console.log("Bye,World!");
},2000);

//(iv)
setTimeout(
    function(){
        console.log("See you there")
}
,5000);

//(v)
(
function(){
    console.log("I am Well executed");
}
)();

//Recursive Functions
function countdown(x){
    console.log(x);
    x = x-1;
    if(x>0){
        countdown(x);
    }
}
countdown(10);