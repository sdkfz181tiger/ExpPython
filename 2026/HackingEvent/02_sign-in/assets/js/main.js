/*
 * Hacking Event
 */

window.onload = ()=>{
	console.log("onload")

	// Click
	document.querySelector("#signIn").onclick = ()=>{
		console.log("Let's sign in...!?");

		// ID
		const id = document.querySelector("#floatingInput").value;
		const pass = document.querySelector("#floatingPassword").value;
		console.log(id, pass);
	}
}

const signIn = (id, pass)=>{
	console.log("signIn:", id, pass);
	if(id == "admin" && pass=="password"){
		return true;
	}
	return false;
}