/*
 * Utility
 */

const sleep = (msec)=>{
   return new Promise(function(resolve) {
      setTimeout(()=>{resolve()}, msec);

   });
}

const signIn = async (id, pass)=>{
	console.log("signIn:", id, pass);
	if(id == "" || pass == "") return false;
	await sleep(40);// Sleep
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