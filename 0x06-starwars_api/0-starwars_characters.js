#!/usr/bin/node

// Import required modules
const request = require('request');

// Function to fetch characters based on Movie ID
function getCharacters (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // Make a GET request to the Star Wars API films endpoint
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching data from Star Wars API:', error.message);
      return;
    }

    // Extract the characters array from the response
    const characters = body.characters;

    // Print each character name
    characters.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error('Error fetching character data:', characterError.message);
          return;
        }
        console.log(characterBody.name);
      });
    });
  });
}

// Read the Movie ID from the command line arguments
const movieId = process.argv[2];

// Check if Movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID as a command line argument.');
  process.exit(1);
}

// Call the function with the provided Movie ID
getCharacters(movieId);
