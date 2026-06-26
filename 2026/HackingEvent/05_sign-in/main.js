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
		

		// 1st try!!
		const id = "ito";
		for(let i=0; i<1000; i++){
			const pass = n2s(3, i);
			console.log(id, pass);
			const result = await signIn(id, pass);// 認証時間がかかる
			if(result){
				console.log("Success:", id, pass);
				return;
			}
		}

		// 2nd try!!
		// const id = "yamada";
		// for(let m=10; m<=12; m++){
		// 	for(let d=1; d<=31; d++){
		// 		const pass = n2s(2, m) + n2s(2, d)
		// 		const result = await signIn(id, pass);// 認証時間がかかる
		// 		if(result){
		// 			console.log("Success:", id, pass);
		// 			return;
		// 		}
		// 	}
		// }

		console.log("Failed...");
	}
}

//==========
// p5js

function setup() {
    createCanvas(windowWidth, windowHeight).parent("canvas");
    noLoop();
}

function draw() {
    background(0, 0, 0, 0);// Transparent
    circle(100, 100, 50);
}