$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    const filmResult = response.results;
    filmResult.forEach(function (item) {
      $('UL#list_movies').append($('<li></li>').text(item.title));
    });
  },
  error: function (xhr, status, error) {
    console.error(status, error);
  }
});
