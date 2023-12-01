#!/usr/bin/node
const request = require('request');
const aprUrl = 'https://jsonplaceholder.typicode.com/todos';

// makes request to the API Url
request(aprUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  // parsin' the response to the body
  const todos = JSON.parse(body);

  // create a map to store # of completed tasks per user
  const completedTasksByUser = { todos };

  // iterate through tasks
  todos.forEach((task) => {
    if (task.completed) {
      completedTasksByUser[task.userId] = (
        completedTasksByUser[task.userId] || 0) + 1;
    }
  });
  // print dem results!
  console.log(JSON.stringify(completedTasksByUser, null, 2));
});
