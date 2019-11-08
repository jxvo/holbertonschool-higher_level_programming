$(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $.getJSON(
      'https://www.fourtonfish.com/hellosalut/?lang=' + lang,
      (body) => $('div#hello').text(body.hello)
    );
  });
});
