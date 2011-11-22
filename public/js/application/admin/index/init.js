/**
 * Created by PyCharm.
 * User: pivo
 * Date: 21.11.11
 * Time: 0:48
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function()
{
	$.jstree._themes = "/public/css/jquery/jstree/";
	$('#jstree').bind("change_state.jstree",
			function(e, data)
			{
				var $obj = data.rslt;
				var id = $obj.data('jstree').id;
				var title = $obj.text();
				if (data.rslt.hasClass('jstree-checked'))
				{
					$.ajax({
						url: '/admin/add',
						data:{
							id:id,
							title:title
						},
						dataType:'json',
						type:'POST',
						success:function(json)
						{
							console.log(json);
						}
					});
				}
				else
				{
					$.ajax({
						url: '/admin/remove',
						data:{id:id},
						dataType:'json',
						type:'POST',
						success:function(json)
						{
							console.log(json);
						}
					});
				}
				console.log(e);
				console.log(data);
				console.log(data.rslt.data('jstree'));
			}).jstree({
				core:{
					animation:200
				},
				types:{
					folder:{
					}
				},
				json_data:{
					ajax:{
						url: "/admin/docstree",
						data
								:
								function(n)
								{
									if (n.data)
										return {id:n.data("jstree").id}
								}
					}
				}		,
				plugins : [ "themes", "json_data", "checkbox",  'ui' ]
			});
});