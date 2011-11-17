/**
 * Created by PyCharm.
 * User: pivo
 * Date: 17.11.11
 * Time: 2:11
 * To change this template use File | Settings | File Templates.
 */
var mouse_coords_30 = {
	statistic:[],
	current_coord:null,
	send_url:'/empty',
	interval_id:null,
	init:function($div) {
		// подсказка в углу экрана. Инициализация. мелкий костыль. Обычный способ инициализации.
		// В даной задаче было бы правильнее прописать объект прямо инициализаторе.
		div_30.init($div);

		// инициализация значений по умолчанию. Чтобы не ставить лишний раз проверку на существование при каждом цикле.
		this.current_coord = new coords();
		this.current_coord.time = new Date();

		// включение событий и интервалов действий.

		// привязка на нажатие клавиши мыши. Включить выключить отправку на сервер каждую 1сек.
		events_30.on_off_event();
		// привязка к движению мыши по экрану. При этом запись в массив не происходит.
		events_30.mousemove();
		// интервал. Сохранение данных о положении курсора в общий массив. С временем его пребывания там.
		// интервал. Отправка на сервер данных каждую 1сек.
		events_30.send_to_server();
	},
	// отправка координат на сервер
	send_coords:function() {
		/*
		 логика такая: .
		 */
		mouse_coords_30.add_coords();
		// некоторая хитрость. Берем копию массива. Хотел сделать чистку на метод success. Но за это время массив сильно измениться. Часть данных будет утеряна.
		var coords = [].concat(mouse_coords_30.statistic);
		// на прод вырезаем. Сейчас можно посмотреть.
		console.log(coords);
		mouse_coords_30.clear_coords();
		// есть возможность посылать кроссдоменно. cookie в header будет передаваться если задать нужный параметр. (docs api jquery).
		$.ajax({
			url:mouse_coords_30.send_url,
			data:coords,
			type:'POST',
			dataType: 'json',
			success:function(json) {

			}
		});
	},
	set_coords:function(layerX, layerY) {
		this.current_coord.time = new Date();
		this.current_coord.x = layerX;
		this.current_coord.y = layerY;
	},
	add_coords:function() {
		// добавление новой координаты в общий массив.

		var point = new coords();
		point.x = mouse_coords_30.current_coord.x;
		point.y = mouse_coords_30.current_coord.y;
		point.time = new Date - mouse_coords_30.current_coord.time;
		mouse_coords_30.statistic.push(point);
	},
	// чистим координату
	clear_coords:function() {
		this.statistic = [];
	}
};

// объект координаты. Прототипы сунуть было некуда. =)
function coords() {
	this.x = 0;
	this.y = 0;
	this.time = 0;
}

// объект с методами событий и интервалов.
var events_30 = {
	interval_id:null,

	interval_id_savepos:null,
	// интервал отправки сообщений на сервер
	timer_send:30,
	// интервал записи в общий массив координат
	timer_savepos: 30,

	mousemove: function() {
		$(window).mousemove(function(evt) {
			mouse_coords_30.set_coords(evt.layerX, evt.layerY);
			// подсказка координат, можно удалить.
			div_30.render(evt.layerX, evt.layerY);
		});
	},
	on_off_event:function() {
		$(window).click(function() {
			// если таймер был создан, то удалим.
			if (events_30.interval_id) {
				clearInterval(events_30.interval_id);
				events_30.interval_id = null;
			}
			else {
				// навесим событие отправки на сервер данных.
				events_30.interval_id = setInterval(mouse_coords_30.send_coords, events_30.timer_send);
			}
		});
	},
	send_to_server:function() {
		// навесим событие отправки на сервер данных.
		events_30.interval_id = setInterval(mouse_coords_30.send_coords, events_30.timer_send);
	}
};

// div элемент с координатами текущего положения курсора.
var div_30 = {
	div:null,
	init:function($div) {
		div_30.div = $div;
	},
	render:function(x, y) {
		div_30.div.html(div_30.template(x, y));
	},
	template:function(x, y) {
		return '<div>' + x + ' ' + y + '</div>';
	}
}