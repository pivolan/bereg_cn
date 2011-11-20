/**
 * Created by PyCharm.
 * User: pivo
 * Date: 21.11.11
 * Time: 0:48
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function() {
	$.jstree._themes = "/public/css/jquery/jstree/";
	$('#jstree').jstree({
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
						function(n) {
							console.log(n.data ? n.data("jstree").id : n);
							if (n.data)
								return {id:n.data("jstree").id}
						}
			}
		}
		,
		plugins : [ "themes", "json_data", "types", "checkbox", "contextmenu", "crrm", 'ui' ]
	});
});