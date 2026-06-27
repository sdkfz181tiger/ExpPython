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
			showToast(result);
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

console.log(p5.prototype.VERSION);

const OFFSET_Y = 24;
const FONT     = "./assets/p5js/fonts/PixelMplus10-Bold.ttf";
let lines      = [];

function setup() {
    //console.log("setup!!");
    createCanvas(windowWidth, windowHeight).parent("canvas");
	background(0, 0, 0, 0);// Transparent
	frameRate(8);
	noStroke();
	loadFont(FONT).then((font)=>{
		textFont(font);
	});
	pushLine();// Test
}

function draw() {
    //console.log("draw!!");
	if(lines.length <= 0) return;
    background(33);// Transparent

	// Draw all lines or delete
	for(let i=lines.length-1; 0<=i; i--){
		if(lines[i].isDead()){
			lines.splice(i, 1);
		}else{
			lines[i].draw();
		}
	}
}

function pushLine(){
	// Push new line
	if(lines.length < 30){
		for(let i=0; i<2; i++){
			const x = random(0, width);
			const y = random(0, -100);
			const size = random(12, 24);
			const sLine = new StrLine(x, y, size);
			lines.push(sLine);
		}
	}else{
		return;
	}
	const rdm = 8000 * Math.random();
	setTimeout(()=>{pushLine();}, rdm);
}