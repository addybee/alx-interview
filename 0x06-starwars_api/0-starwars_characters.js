#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function requestPromise(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) return reject(error);
      if (response.statusCode !== 200) return reject(new Error(`Failed with status code ${response.statusCode}`));
      resolve(JSON.parse(body).name);
    });
  });
}

function callback(error, resp, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (resp.statusCode === 200) {
    const movieCharacters = JSON.parse(body).characters;

    const characterPromises = movieCharacters.map(charUrl => requestPromise(charUrl));

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error('Error fetching character names:', error);
      });
  } else {
    console.error(`Failed to fetch movie. Status code: ${resp.statusCode}`);
  }
}

request(movieUrl, callback);
