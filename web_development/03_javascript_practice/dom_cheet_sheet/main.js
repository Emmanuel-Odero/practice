/*// Examine The Document Object
//console.dir(document)  //gives the properties and methods used in our site
console.log(document.domain) //gives the domain we are running
console.log(document.URL)
console.log(document.title)
document.title = "new title"; //making changes for this case the title is changed
console.log(document.doctype)
console.log(document.head)
console.log(document.all) //Gives an array of all the HTML elements in our DOM
console.log(document.forms)
console.log(document.links)
console.log(document.images)



//GETELEMENTSBYID

var headerTitle = document.getElementById('header-title')
var header = document.getElementById('main-header')
headerTitle.textContent = "Hello"; //textContent disregards the settings and styling of internal elements
headerTitle.innerText = "Goodbye"; //Takes account of the styles included in the child elements
headerTitle.innerHTML = "<h2> Hellow </h2>" // inputs the h2 inside the h1 like for this case

headerTitle.innerHTML = "Item Lister" //transforming to the initial state
header.style.borderBottom = 'solid 3px black'; //change styling NB:the style is written in camelcase format


//GETELEMENTSBYCLASSNAME
var items = document.getElementsByClassName('list-item'); //Gives an array of list objects

items[1].style.backgroundColor = 'Red';

//GETELEMENTSBYTAGNAME
var items = document.getElementsByTagName('li'); //Gives an array of list objects

items[4].style.backgroundColor = 'Yellow';


// QUERYSELECTOR //

//NB: Note that this only applies to one variable even if many exists within the document. 
//To select many at once. Please use querySelectorAll() instead

var header = document.querySelector('#main-header');
header.style.borderBottom = "solid 4px #ccc";


// QUERYSELECTORALL //

var odd = document.querySelectorAll('li:nth-child(odd)');
var even = document.querySelectorAll('li:nth-child(even)');

for (var i = 0; i < odd.length; i++){
	odd[i].style.backgroundColor  ='lightgrey';
	even[i].style.backgroundColor  ='darkgrey';
}; */



/*

// TRAVERSING THE DOM //

var itemList = document.querySelector('#items');

//parentNode
itemList.parentNode.style.backgroundColor ='lightgrey';

//parentElement is the same as parenNode in most cases and can be used interchangebly.

//childNodes
//Gives all an array of child nodes within the itemList ID.note that for cases like this
 //where we have different lines it will also take account of the line breaks and for this case it will 
 //be printed as a text item in the array hence taking an index
console.log(itemList.childNodes);

//children
//Gives an array like childNodes abouve but doesn't include the text as a child hence the 
//	best use case for child related actions.
console.log(itemList.children)

//firstChild
// This will inherit from childNode hence the first item to be listed in this case will be
	text. Example below best describes this scenario. //
console.log(itemList.firstChild)


//firstElementChild  
// Best use case for child access instead of first child which is considered useless.//
console.log(itemList.firstElementChild)

//lastChild and lastElementChild
// NB: these behaves the same as firstChild and lastElementChild only that they focus on the last elements

//nextSibling and nextElementSibling to access the siblings of the current element.

//previousSibling and previousElementSibling to access the siblings before the current element.

//createElement
var newDiv = document.createElement('div')

newDiv.className = 'hello'; //give our new element a class name
newDiv.id = 'hello1';  //give our new element an id name
newDiv.setAttribute('src', 'www.google.com'); //set an extra attribute eg src="www.google.com"

//create textNode
var newDivText = document.createTextNode('Hello World');


//append text to div
newDiv.appendChild(newDivText)

console.log(newDiv)

//insert the new created element to header before h1
var container = document.querySelector('header .container');
var h1 = document.querySelector('header h1')

container.insertBefore(newDiv, h1) */



//Events Handling

var button = document.getElementById('button');

button.addEventListener('click', buttonClick)


//accessing some of the attributes of event object
function buttonClick(e){
	console.log(e.target);
	console.log(e.target.id)
	console.log(e.target.className)
	console.log(e.target.classList)
	console.log(e.type)
	console.log(e.clientx); //mouse x position
	console.log(e.clienty); //mouse y position
}

//Mouse Actions: click, dblclick, mousedown, mouseup, mouseenter, mouseleave, mouseover,mouseout
//  mousemove

//Keyboard Events
	//keydown - fires everytime an input is received from the keyboard.
	//keyup
	//keypress


// Other input into eventhandlers
	//focus - when you just click on an input
	//blur - when we move out of the focus
	//cut - used for cutting a text
	//paste - used to paste the item we cutted
	//input
	//change - mostly used for select inputs 

var itemInput = document.querySelector('input[type="text"]');
var form = document.querySelector('form');


