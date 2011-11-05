/**
 * Created by PyCharm.
 * User: pivo
 * Date: 05.11.11
 * Time: 19:29
 * To change this template use File | Settings | File Templates.
 */

var autoreplace = {
	defualt_color: 'black',
	empty_color: '#908e8e',
	init: function(){
		$('.replace_empty').focus(function() {
					if ($(this).val() == this.defaultValue) {
						$(this).val('').css("color", autoreplace.defualt_color).css('font-style', 'normal');
					}
				}
		);
		$('.replace_empty').blur(function() {
			if ($(this).val() == '') {
				$(this).css("color", autoreplace.empty_color).css('font-style', 'italic').val(this.defaultValue);
			}
		});
	}
};