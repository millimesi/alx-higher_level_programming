$(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      const charName = response.hello;
      displayName(charName);
    },
    error: function (xhr, status, error) {
      console.error(status, error);
    }
  });
  function displayName (charName) {
    $('DIV#hello').text(charName);
  }
});
