

const registrationForm = document.querySelector('#registrationForm');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const idNumberInput  = document.querySelector('#idNumber');
const submit = document.querySelector('.submit-btn');
const msg = document.querySelector('.msg')
const userList = document.querySelector('#users')

submit.addEventListener('click', onSubmit); //not that this listiner can use both the form or submit to listen

function onSubmit(e){
	e.preventDefault();

	if (nameInput.value === '' || emailInput.value === '' || idNumberInput.value === '') {
		msg.classList.add('error') //adds the error class to this element
		msg.innerHTML = 'Please enter all fields';

		setTimeout(()=>msg.remove(), 3000); //displays the message for 3 seconds. Note this takes 2 arguments (function, time)
	} else {
		const li = document.createElement('li'); //creates an element from no where
		li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value} : ${idNumberInput.value}`)); //appends the data we want
		userList.appendChild(li);

		//now clear the list once all these function steps are complited and submited
		nameInput.value = '';
		emailInput.value = '';
		idNumberInput.value = '';
	};
}