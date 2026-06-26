/*
 * Utility
 */

const n2s = (pad, num)=>{
	return String(num).padStart(pad, "0");
}

const sleep = (msec)=>{
   return new Promise(function(resolve) {
      setTimeout(()=>{resolve()}, msec);

   });
}

const signIn = async (id, pass)=>{
	console.log("signIn:", id, pass);
	if(id == "" || pass == "") return false;
	await sleep(300);// Sleep
	for (const user of data) {
		if (id == user.id && pass == user.pass){
			return true;
		}
	}
	return false;
}

const loadJson = async (path)=>{
	console.log("loadJson:", path);
	try {
		const response = await fetch(path);
		if (!response.ok) {
			throw new Error("Failed");
			return null;
		}
		const data = await response.json();
		return data;
	} catch (error) {
		console.error(error);
		return null;
	}
}

//==========
// p5js

class StrLine{

	constructor(x, y, size){
		this._x = x;
		this._y = y;
		this._size = size;
		let cObj = new CharObj(0, x, y, size);
		this._arr = [];
		this._arr.push(cObj);
	}

	draw(){
		if(this.isDead()) return;
		// Push new character
		let length = this._arr.length;
		let x = this._x;
		let y = this._arr[length-1].getY() + OFFSET_Y;
		if(y < windowHeight){
			let cObj = new CharObj("A", x, y, this._size);
			this._arr.push(cObj);
		}
		// Draw all characters or delete
		for(let i=this._arr.length-1; 0<=i; i--){
			if(this._arr[i].isDead()){
				this._arr.splice(i, 1);
			}else{
				this._arr[i].draw();
			}
		}
	}

	isDead(){
		if(0 < this._arr.length) return false;
		return true;
	}
}

class CharObj{

	constructor(c, x, y, size){
		this._c = c;
		this._x = x;
		this._y = y;
		this._size = size;
		this._r = 50;
		this._g = 255;
		this._b = 100;
		this._a = floor(random(100, 255));
	}

	draw(){
		this._c = floor(random(0, 2));
		this._a -= 10;
		fill(this._r, this._g, this._b, this._a);
		textSize(this._size);
		text(this._c, this._x, this._y);
	}

	getX(){return this._x;}
	getY(){return this._y;}

	isDead(){
		if(0 < this._a) return false;
		return true;
	}
}