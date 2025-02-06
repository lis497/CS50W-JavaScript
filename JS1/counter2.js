let counter = 0;
function count(){
	counter ++;
	//console.log(counter)
	document.querySelector("h1").innerHTML=`Hello ${counter}!`;
	if (counter % 10 === 0) {
		alert(`Counter is now ${counter}`);
	}	
}

//callback function
document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('button').innerHTML = "Meow"
	// onclick must be lower case
	//document.querySelector('button').onclick = count;
	// important: in js use count, in html use onclick='count()'
	//both of them work, event {click, DOMContentLoaded ...}
	document.querySelector('button').addEventListener('click', count);
}) 