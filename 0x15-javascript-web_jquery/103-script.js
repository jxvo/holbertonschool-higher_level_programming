function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  const language = $('input#language_code').val();
  const object = { lang: lang };
  $.getJSON(url, object, (body) => $('div#hello').text(body.hello));
}

$(function () {
  $('input#btn_translate').on('click', translate);
  $('input#language_code').on('keydown', function (event) {
    if (event.keyCode === 13) { translate(); }
  });
});
