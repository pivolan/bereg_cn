function hide1(child) {
	child.stop().slideUp('fast', function() {
		$(this).removeAttr('open')
	});
}
function collapsElement(id) {
	$('#' + id).stop().attr('height', 'auto').slideToggle('fast');
}

$(document).ready(function() {              // по окончанию загрузки страницы
	$('div.service').slideUp(0);
	$('.replace_empty').focus(function() {
				if ($(this).val() == this.defaultValue) {
					$(this).val('').css("color", "black").css('font-style', 'normal');
				}
			}
	);
	$('.replace_empty').blur(function() {
		if ($(this).val() == '') {
			$(this).css("color", "#908e8e").css('font-style', 'italic').val(this.defaultValue);
		}
	});
	$('li.link').hover(function() {
				console.log(this);
				var child = $(this).find('ul.submenu');
				var offset = $(this).find('a.link').offset();
				var x = offset.left - 10;
				var y = offset.top + 40;
				child.css({height:'auto'}).stop();
				child.css({top:y + "px",left:x + "px"}).slideDown('fast',
						function() {
							$(this).attr('open', 'open')
						});
			},
			function() {
				var child = $(this).find('ul.submenu');
				setTimeout(function(){
					hide1(child);
				}, 0);
			}
	);

});   //document ready end
function coll() {
	$('#feedback').slideToggle('fast');
}

