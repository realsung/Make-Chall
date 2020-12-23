const express = require('express');
const fs = require('fs');

const app = express();

// const FLAG = "GOHACK{c595629b13140d64413d420bb8df025c}";

app.get('/', (req, res) => {
	res.send("BabyWeb Challenge");
	// res.redirect("https://youtu.be/q6EoRBvdVPQ");
});

app.get('/list', (req, res) => {
	// const param = req.query.image;
	// var path1 = url.parse(req.url, true).query['image'];
	// if(!param) return status(403).send("FORBIDDEN ^___^");
	try{
		const param = req.query.image;
		if(!param) return status(403).send("FORBIDDEN ^___^");
		if (param.indexOf("..") == -1) {
			const path = decodeURI(__dirname + "/images/" + param);
			console.log(path);
			if(fs.existsSync(path)){
				fs.readFile(path, (err, data) => {
					if (err) {
						return res.status(500).send("Internal Server Error");
					}
					res.contentType(param);
					res.status(200).end(data);
				});
			}else{
				res.status(404).send("File doesn't exist!! ^^..");
			}
		}else{
			res.status(403).send("FORBIDDEN @.@");
		}
	} catch(err){
		res.status(500).send("Internal Server Error");
	}
});

app.get('/filelist', (req, res) =>{
	try{
		fs.readdir(__dirname + "/images", (err, data) => {
			if (err) throw err;
			res.status(200).send(data);
		});
	} catch(err){
		res.status(500).send("Internal Server Error");
	}
});

app.listen(2581, () => {
	console.log('START UP!');
});
