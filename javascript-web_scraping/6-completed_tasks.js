#!/usr/local/bin/node
const request = require('request');
const apiUrl = process.argv[2];


  // create a map to store # of completed tasks per user
  const completedTasksByUser = {};
// makes request to the API Url
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  // parsin' the response to the body
  const todos = JSON.parse(body);

  // iterate through tasks
  todos.forEach((task) => {
    if (task.completed) {
      completedTasksByUser[task.userId] = (
        completedTasksByUser[task.userId] || 0) + 1;
    }
  });
  // print dem results!
  console.log(completedTasksByUser);
});
