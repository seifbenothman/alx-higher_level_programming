/* globals $ */
$(function () {
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();

    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      if (data && data.hello) {
        $('#hello').text(data.hello);
      } else {
        $('#hello').text('Translation not found');
      }
    });
  }
});
