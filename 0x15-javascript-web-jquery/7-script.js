$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (resp) => {
  $('#character').text(resp.name);
});
