$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (resp) => {
  resp.results.forEach((film) => {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});