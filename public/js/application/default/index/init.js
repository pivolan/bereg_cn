/**
 * Created by PyCharm.
 * User: pivo
 * Date: 17.11.11
 * Time: 2:11
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function(){
	// каждые 30мс взятие одной координаты мыши. отправка каждую секунду.
	//mouse_coords.init($('#coord'));
	// каждые 30мс отпавка на сервер. Сбор всего что пришло за 30мс.
	mouse_coords_30.init($('#coord'));
});