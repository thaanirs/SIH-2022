const { query } = require('express');
var mysql = require('mysql2');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root"
});

con.connect(function(err) {
  if (err) 
    console.log(err);
  console.log("Connected!");
  let QUERY = "CREATE DATABASE networkflow";
  con.query(`${QUERY}`,function(err,result){
    if(err)
        throw err;
    console.log("database created");
  })
});

