/**
 * Created by PyCharm.
 * User: pivo
 * Date: 17.11.11
 * Time: 2:11
 * To change this template use File | Settings | File Templates.
 */
var mouse_coords = {
	statistic:[],
	current_coord:null,
	previous_coord:null,
	send_url:'/empty',
	interval_id:null,
	init:function($div) {
		// подсказка в углу экрана. Инициализация. мелкий костыль. Обычный способ инициализации.
		// В даной задаче было бы правильнее прописать объект прямо инициализаторе.
		div.init($div);

		// инициализация значений по умолчанию. Чтобы не ставить лишний раз проверку на существование при каждом цикле.
		this.current_coord = new coords();
		this.current_coord.time = new Date();
		this.previous_coord = new coords();
		this.previous_coord.time = new Date();

		// включение событий и интервалов действий.

		// привязка на нажатие клавиши мыши. Включить выключить отправку на сервер каждую 1сек.
		events.on_off_event();
		// привязка к движению мыши по экрану. При этом запись в массив не происходит.
		events.mousemove();
		// интервал. Сохранение данных о положении курсора в общий массив. С временем его пребывания там.
		events.savepos();
		// интервал. Отправка на сервер данных каждую 1сек.
		events.send_to_server();
	},
	set_coords:function(layerX, layerY) {
		this.current_coord.time = new Date();
		this.current_coord.x = layerX;
		this.current_coord.y = layerY;
	},
	// отправка координат на сервер
	send_coords:function() {
		/*
		 логика такая: если координата курсора не менялась, то общая функция не записывала ее в общий массив, до тех пор пока она не изменится.
		 Однако перед отправкой на сервер не плохо бы знать последнее положение курсора, и сколько он там пробыл. Поэтому делаем
		 обязательное присвоение последней координаты и вычисляем для нее время пребывания. При этом current_coord не портим.
		 Чтобы время пребывания в этой точке в итоге было полным.
		 */
		if (mouse_coords.compare()) {
			mouse_coords.save_last();
		}
		// некоторая хитрость. Берем копию массива. Хотел сделать чистку на метод success. Но за это время массив сильно измениться. Часть данных будет утеряна.
		var coords = [].concat(mouse_coords.statistic);
		// на прод вырезаем. Сейчас можно посмотреть.
		console.log(coords);
		mouse_coords.clear_coords();
		// есть возможность посылать кроссдоменно. cookie в header будет передаваться если задать нужный параметр. (docs api jquery).
		$.ajax({
			url:mouse_coords.send_url,
			data:coords,
			type:'POST',
			dataType: 'json',
			success:function(json) {

			}
		});
	},
	compare:function() {
		// сравнение предыдущей координаты и новой
		return (this.previous_coord.x == this.current_coord.x) && (this.previous_coord.y == this.current_coord.y);
	},
	save_last:function() {
		var point = new coords();
		point.x = mouse_coords.current_coord.x;
		point.y = mouse_coords.current_coord.y;
		point.time = new Date - mouse_coords.current_coord.time;
		mouse_coords.statistic.push(point);
	},
	add_coords:function() {
		// добавление новой координаты в общий массив.

		// если предыдущая координата не равна текущей.
		if (!mouse_coords.compare()) {
			var point = new coords();
			point.x = mouse_coords.current_coord.x;
			point.y = mouse_coords.current_coord.y;
			point.time = new Date - mouse_coords.current_coord.time;
			mouse_coords.statistic.push(point);
		}
		// присваиваем прошлой координате текущую. Делаем это через создание нового объекта. Иначе была бы ссылка.
		mouse_coords.previous_coord = new coords();
		mouse_coords.previous_coord.x = mouse_coords.current_coord.x;
		mouse_coords.previous_coord.y = mouse_coords.current_coord.y;
		mouse_coords.previous_coord.time = mouse_coords.current_coord.time;
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
var events = {
	interval_id:null,

	interval_id_savepos:null,
	// интервал отправки сообщений на сервер
	timer_send:1000,
	// интервал записи в общий массив координат
	timer_savepos: 30,

	mousemove: function() {
		$(window).mousemove(function(evt) {
			mouse_coords.set_coords(evt.layerX, evt.layerY);
			// подсказка координат, можно удалить.
			div.render(evt.layerX, evt.layerY);
		});
	},
	on_off_event:function() {
		$(window).click(function() {
			// если таймер был создан, то удалим.
			if (events.interval_id) {
				clearInterval(events.interval_id);
				events.interval_id = null;
			}
			else {
				// навесим событие отправки на сервер данных.
				events.interval_id = setInterval(mouse_coords.send_coords, events.timer_send);
			}
		});
	},
	savepos:function() {
		// сохраним координаты в общий массив.
		this.interval_id_savepos = setInterval(mouse_coords.add_coords, events.timer_savepos);
	},
	send_to_server:function() {
		// навесим событие отправки на сервер данных.
		events.interval_id = setInterval(mouse_coords.send_coords, events.timer_send);
	}
};

// div элемент с координатами текущего положения курсора.
var div = {
	div:null,
	init:function($div)
	{
		div.div = $div;
	},
	render:function(x, y) {
		div.div.html(div.template(x, y));
	},
	template:function(x, y) {
		return '<div>' + x + ' ' + y + '</div>';
	}
}