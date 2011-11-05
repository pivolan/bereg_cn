function collapsElement(id) {
	$('#' + id).stop().attr('height', 'auto').slideToggle('fast');
}

$(document).ready(function() {              // по окончанию загрузки страницы
	$('div.service').slideUp(0);
});   //document ready end
