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
					types:{
						document:{
							icon: {
								image: '/public/img/catalogue/docment_16.png'
							}
						},
						root:{
							icon: {
								image: '/public/img/catalogue/root_16.png'
							}
						}
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
				plugins : [ "themes", "json_data", "checkbox",  'ui', 'crrm', 'dnd', 'types', 'contextmenu', 'cookies']
			}).bind("create.jstree", function (e, data)
			{
				$.post(
						"/static/v.1.0pre/_demo/server.php",
						{
							"operation" : "create_node",
							"id" : data.rslt.parent.attr("id").replace("node_", ""),
							"position" : data.rslt.position,
							"title" : data.rslt.name,
							"type" : data.rslt.obj.attr("rel")
						},
						function (r)
						{
							if (r.status)
							{
								$(data.rslt.obj).attr("id", "node_" + r.id);
							}
							else
							{
								$.jstree.rollback(data.rlbk);
							}
						}
				);
			})
			.bind("remove.jstree", function (e, data)
			{
				data.rslt.obj.each(function ()
				{
					$.ajax({
						async : false,
						type: 'POST',
						url: "/static/v.1.0pre/_demo/server.php",
						data : {
							"operation" : "remove_node",
							"id" : this.id.replace("node_", "")
						},
						success : function (r)
						{
							if (!r.status)
							{
								data.inst.refresh();
							}
						}
					});
				});
			})
			.bind("rename.jstree", function (e, data)
			{
				$.post(
						"/static/v.1.0pre/_demo/server.php",
						{
							"operation" : "rename_node",
							"id" : data.rslt.obj.attr("id").replace("node_", ""),
							"title" : data.rslt.new_name
						},
						function (r)
						{
							if (!r.status)
							{
								$.jstree.rollback(data.rlbk);
							}
						}
				);
			})
			.bind("move_node.jstree", function (e, data)
			{
				data.rslt.o.each(function (i)
				{
					$.ajax({
						async : false,
						type: 'POST',
						url: "/static/v.1.0pre/_demo/server.php",
						data : {
							"operation" : "move_node",
							"id" : $(this).attr("id").replace("node_", ""),
							"ref" : data.rslt.cr === -1 ? 1 : data.rslt.np.attr("id").replace("node_", ""),
							"position" : data.rslt.cp + i,
							"title" : data.rslt.name,
							"copy" : data.rslt.cy ? 1 : 0
						},
						success : function (r)
						{
							if (!r.status)
							{
								$.jstree.rollback(data.rlbk);
							}
							else
							{
								$(data.rslt.oc).attr("id", "node_" + r.id);
								if (data.rslt.cy && $(data.rslt.oc).children("UL").length)
								{
									data.inst.refresh(data.inst._get_parent(data.rslt.oc));
								}
							}
							$("#analyze").click();
						}
					});
				});
			});

	$("#mmenu input").click(function ()
	{
		switch (this.id)
		{
			case "add_document":
			case "add_folder":
				$("#jstree").jstree("create", null, "last", { "attr" : { "rel" : this.id.toString().replace("add_", "") } });
				break;
			case "search":
				$("#jstree").jstree("search", document.getElementById("text").value);
				break;
			case "text":
				break;
			default:
				$("#jstree").jstree(this.id);
				break;
		}
	});
});