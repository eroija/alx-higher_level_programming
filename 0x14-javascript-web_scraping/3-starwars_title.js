#!/usr/bin/node
const request = require('request');

const episodeNumber = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieData = JSON.parse(body);
    console.log(`Title of Episode ${episodeNumber}: ${movieData.title}`);
  }
});
