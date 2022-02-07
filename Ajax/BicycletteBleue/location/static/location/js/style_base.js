/* Premier test

$.fn.datepicker.defaults.format = "mm/dd/yyyy";
$('.datepicker').datepicker({
    format: 'mm/dd/yyyy',
    startDate: '-3d'
});
var datepicker = $.fn.datepicker.noConflict(); // return $.fn.datepicker to previously assigned value
$.fn.bootstrapDP = datepicker;                 // give $().bootstrapDP the bootstrap-datepicker functionality


*/

/* Troisième calendrier bootstrap */


$(document).ready(function(){

$('.datepicker').datepicker({
format: 'dd-mm-yyyy',
autoclose: true,
startDate: '0d'
});

$('.cell').click(function(){
$('.cell').removeClass('select');
$(this).addClass('select');
});

});