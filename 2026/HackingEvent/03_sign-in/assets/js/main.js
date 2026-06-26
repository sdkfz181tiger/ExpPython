/*
 * Hacking Event
 */

let data = null;

window.onload = ()=>{
	console.log("onload");

	// Data
	loadJson("./data/data.json").then(jObj=>{
		data = jObj.data
	});

	// Click
	document.querySelector("#signIn").onclick = async ()=>{
		const id = document.querySelector("#floatingInput").value;
		const pass = document.querySelector("#floatingPassword").value;
		signIn(id, pass).then(result=>{
			console.log("signIn:", result);
		});
	}

	// Test
	document.querySelector("#test").onclick = async ()=>{
		
		const id = "yamada";

		// 1st try!!
		// for(let i=0; i<1230; i++){
		// 	const pass = "pass_" + i;
		// 	console.log(id, pass);
		// 	const result = await signIn(id, pass);
		// 	if(result){
		// 		console.log("Success:", id, pass);
		// 		return;
		// 	}
		// }

		// 2nd try!!
		for(let m=1; m<=12; m++){
			for(let d=1; d<=31; d++){
				const pass = "pass_" + n2s(m) + n2s(d)
				const result = await signIn(id, pass);
				if(result){
					console.log("Success:", id, pass);
					return;
				}
			}
		}

		console.log("Failed...");
	}
}