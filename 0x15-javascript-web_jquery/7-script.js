$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    const charName = response.name;
    displayName(charName);
  },
  error: function (xhr, status, error) {
    console.error(status, error);
  }
});

function displayName (charName) {
  $('DIV#character').text(charName);
}
