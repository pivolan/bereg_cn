/**
 * Created by PyCharm.
 * User: pivo
 * Date: 05.11.11
 * Time: 19:26
 * To change this template use File | Settings | File Templates.
 */
var menu_top = {
	init: function() {
		$('li.link').hover(function() {
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
					setTimeout(function() {
						menu_top.collapse(child);
					}, 0);
				}
		);
	},
	collapse: function(child) {
		child.stop().slideUp('fast', function() {
			$(this).removeAttr('open')
		});
	}

};