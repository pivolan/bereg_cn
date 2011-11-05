/**
 * Created by PyCharm.
 * User: pivo
 * Date: 05.11.11
 * Time: 22:20
 * To change this template use File | Settings | File Templates.
 */
var service_slider = {
	init: function()
	{
		$('a.service_slider').click(function(){
			var $this = $(this);
			var $parent = $(this).parent();
			var $child = $(this).parent().next();
			$child.slideToggle('fast');
			if ($this.hasClass('active')){
				$this.removeClass('active');
				$parent.removeClass('active');
			}
			else
			{
				$this.addClass('active');
				$parent.addClass('active');
			}
		});
	}
};