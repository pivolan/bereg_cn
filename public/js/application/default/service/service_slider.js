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
			var $child = $(this).next('p');
			$child.slideToggle('fast', function(){
				if ($this.hasClass('active')){
					$this.removeClass('active');
				}
				else
				{
					$this.addClass('active');
				}
			});
		});
	}
};