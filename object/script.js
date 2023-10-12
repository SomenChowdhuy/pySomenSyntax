//Exercise 1
const person = {
    f_name: "Somen",
    "l_name": "Chowdhury",
    age: 35,
    "height": 5.4,
    "Marital Status": "Unmarried",
    religion: "Buddhism"
};
console.log(typeof person);
console.log(person);
console.log(person.age);
console.log(person['height']);
console.log(person['l_name']);
console.log(person["Marital Status"]);
console.log(person['religion']);
// person["first name"] = 'Mr. Somen"
person.f_name = "Mr. Somen";
console.log(person['f_name']);
person.age = 27;
console.log(person['age']);
person.religion = "Aethist";
console.log(person['religon']);
person.company = "Tesla";
console.log(person);
person.BloodGroup = 'B+';
console.log(person); 
person.height = 5.7;
console.log(person['height']);
person.hometown = "Chittagong";
console.log(person);
delete person["Marital Status"];
delete person.age;
delete person.BloodGroup;
delete person.company;
delete person.hometown;

//exercise 2
//Nested object
const man = {
    firstName: "Elon",
    lastName: "Musk",
    age: 35,
    address:{
        street: "Tesla Road",
        city: "Austin",
        state: "Texas",
        country: "United States",
        zipCode: "78725"
    }
}
console.log(man.address.city);
console.log(man.address.zipCode);

//Check if a property exists in object
console.log("age" in man);
console.log("firstName" in man);
console.log("hometown" in man);
for(let prop in man){
    // console.log(prop);
    // console.log(man[prop]);
    console.log(prop +": "+ man[prop]);
}

//create an object with new keyword
//method (i)
const person1 = new Object();
person1.f_name = 'Elon';
person1.l_name = 'Musk';
person1.age = 35;
console.log(person1);
//method (ii)
const person2 = new Object({
    f_name: 'Elon',
    l_name: 'Musk',
    age: 36
});
console.log(person2);


const person = {
    f_name: 'Elonn',
    l_name: 'Musk',
    age: 37,
    address:{
        street: 'Tesla Road',
        city: 'Austin',
        state: 'Texas',
        country: 'USA',
        zipCode: '78725'
    }
}
//to check if a propery is exist in an object
//syntax
//prop in object_name
console.log('address' in person)
console.log('state' in person.address)
console.log('zipCode' in person.address)


//for....in
//syntax
// for(let prop in obj_name){}

//exercise1
const person = {
    f_name: 'Elonn',
    l_name: 'Musk',
    age: 37,
    address:{
        street: 'Tesla Road',
        city: 'Austin',
        state: 'Texas',
        country: 'USA',
        zipCode: '78725'
    }
}
for(let prop in person.address){
    console.log(prop);
}

//exercise 2
const person = {
    f_name: 'Elonn',
    l_name: 'Musk',
    age: 37,
    address:{
        street: 'Tesla Road',
        city: 'Austin',
        state: 'Texas',
        country: 'USA',
        zipCode: '78725'
    }
}
for(let prop in person.address){
    console.log(person.address[prop]);
}