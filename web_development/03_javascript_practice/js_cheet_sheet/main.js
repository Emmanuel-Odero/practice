alert("Welcome to our webpage")
console.log("Hellow world")
console.error("This is an error")
console.warn("This is a warning")

//let, const  "these are variable declaration methods and don't use var since it set the variable to global state."

let age = 30;
age =  31   //note how the variable changes when let is used but this ain't the case for const
console.log(age)


//Strings, Numbers, Boolean, null, Undefined
const name =  'John';
const ages = 30;
const rating = 4.5; //there is nothing like float in JS and everything is treated as a number datatype
const isCool = true;
const x = null; //data type should be thought of as basically wrong with it being described as object.
const y = undefined;

console.log(typeof name)  //checking the datatype of a variable


//String Concatination
let user = "John";
let level = 3;

console.log('My name is '+ user + ' and am currently in level ' + level)
console.log(`My name is ${user} and am currently in level ${level}`)  //best alternative in string concatination

//Getting the String Length
userLength = user.length    //no braces makes this a property but incase we had braces then a method
userLowerCased = user.toLowerCase()
userUpperCased = user.toUpperCase()
userSubString = user.substring(0,3) //arguments being (start, end)
userSplitted = user.split('') //to split the letters we use just 2 quotes otherwise declare your own terms


console.log(userSubString)
console.log(userLength)
console.log(userSplitted)

//Arrays - These are variables that hold multiple values
let numbers = new Array(1,2,3,4,5); //we can use 'new Array()' constructor to create and array

let fruits = ['Apple', 'Mangoes', 'Orange', 'Pineapple']
fruits.push('Grapes')  //add data to the array, this is same as .append in python
fruits.unshift('Strawberries') //add the data to the beginning of the array
fruits.pop()  //removes the last data in the array
Array.isArray(fruits) //check whether fruits is an array
fruits.indexOf('Orange')  //checks the index of Orange in the fruits array

console.log(fruits)


//Dictionaries
const person = {
	firstName:'Michael',
	lastName:'Ochara',
	age:34,
	hobbies: ['Sports', 'Music', 'Movies'],
	address:{
		street:'Kimathi st',
		city:'Boston',
		state: 'MA'
	}
}

console.log(`${person.firstName} ${person.lastName} is from ${person.address.city}`)

person.email = "michaelochara@gmail.com" //to add something to the object


const todos = [
		{
			id:1,
			text:'Watch a movie today',
			isComplete: true
		},
		{
			id:2,
			text:'Meet Kwamboka by the bus station',
			isComplete: false
		},
		{
			id:3,
			text:'Visit a dentist at Agah Khan Hospital',
			isComplete: true
		},
]

const todoJSON = JSON.stringify(todos)  //convert to JSON type
console.log(todoJSON)



//FOR

for(let i=0; i < todos.length; i++){
	console.log(`${todos[i].text}`)
}

for(let todo of todos){		//the best way to loop an array
	console.log(todo.id)
}


//forEach, map, filter

todos.forEach(function(todo) {
	console.log(todo.text);
});

const todoText = todos.map(function(todo){  //map returns an array
	return todo.text
});
console.log(todoText)

const todoCompleted = todos.filter(function(todo){
	return todo.isComplete === true
});
console.log(todoCompleted)

//IF

// OR = ||
// AND = &&

const h = 10;

if (h == 10){ //double == doesn't take data type into accont while === takes the doubling to accont
	console.log("h is 10")
} else if(h > 10){
	console.log('h is greater than 10')
}else{
	console.log('h is less than 10')
}

//ternary operator also functions like if statements as described in the example below
const w = 10;
const color = w > 10 ? 'red':'blue'  //if x is greater than 10 color=red else color=blue

//another way to go about conditional operators is to use switch statement
switch(color){
	case 'red':
		console.log('The color is red');
		break;
	case 'blue':
		console.log('The color is blue');
		break;
	default:
		console.log('The color is neither red nor blue');
		break;
}

// FUNCTIONS

function addNums(num1=1, num2=2){
	return (num1 + num2)
}

console.log(addNums(5,5))

//aleternative to the function above

const addition = (num1, num2) => num1 + num2;
console.log(addition(5,7))


		// Object Oriented Programming (OOP)

//constructor function
function Person(firstName, lastName, dob){
	this.firstName =firstName;
	this.lastName = lastName;
	this.dob = new Date(dob); //construct a date from the data passed
	this.getBirthYear = function(){
		return this.dob.getFullYear() //this is how we add functions to our person class
	} 
		
	};
	

//the best way to add functions to our Person class, this is a better practice compared to getBirthYear above
//in the console the function below will appear on proto_
Person.prototype.getFullName = function(){
	return `${this.firstName} ${this.lastName}`;
};



//instantiate
const person1 = new Person('Michael', 'Ochara', '4-5-1991')
const person2 = new Person('Elizabeth', 'Njeru', '6-11-1982')

console.log(person1)
console.log(person2.firstName)
console.log(person2.getBirthYear()) //notice getBirthYear has brackets (), since its a method inside a funtion
console.log(person2.getFullName())


//alternative to creating classes using syntactic sugar

class Persons{
	constructor(firstName, lastName, dob){
		this.firstName =firstName;
		this.lastName = lastName;
		this.dob = new Date(dob)
	}

	getBirthYear() {
		return this.dob.getFullYear()
	}

	getFullName() {
		return `${this.firstName} ${this.lastName}`;
	}
}

//Basics of DOM

/**
  window property enable to view everything from the document properties, local storage
  , fetch api etc. This is very useful and to make a view we call it in the next line.
**/
console.log(window);

//single element selectors
const header = document.getElementById('main-header')
const heading = document.querySelector('.site-heading') //just selects one item and for class use '.' id '#'

//multiple element selectors
const products = document.querySelectorAll('.item'); //return an array like result and for this reason its the best to select multiple items
const products1 = document.getElementsByClassName('item') //notice we don't include the . gives html colleciton hence can't be accessed like an array
const products2 = document.getElementsByTagName('li') //will result to an array like object


const ul = document.querySelector('.items')

//ul.remove();  //removes the entire ul list
ul.lastElementChild.remove(); //removes the last element child for ul
ul.firstElementChild.textContent = 'Hello'; //changes the first textContent to hello
ul.children[1].innerText = 'Michael Ochara'
ul.lastElementChild.innerHTML = '<li>Added From Script</li>'


const btn = document.querySelector('.btn')

btn.addEventListener('click', (e) => {
	e.preventDefault();
	document.querySelector('body').style.background = '#ccc';
	btn.style.background='red';
})