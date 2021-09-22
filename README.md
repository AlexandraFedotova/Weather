<h1>Weather </h1>

<p> Веб-сервис получает данные о погоде из публичного API (https://api.openweathermap.org/data/2.5/onecall/timemachine) и производит их агрегацию, после чего возвращает результат. 

Корректный формат запроса к сервису: GET /weather?city=<city>&days=<n>. Например, GET /weather?city=Saint-Petersburg&days=4 </p>

<p>Пример запуска сервиса: </p>
<img alt="GET http://127.0.0.1:5000/weather?city=Saint-Petersburg&days=4" src="README/Request.jpg"> 

<p>Сервис возвращает следующий json ответ: </p>
<img alt="error" src="README/Response.jpg"> 

<p>Запрос был выполнен с помощью платформы Postman (https://www.postman.com/product/what-is-postman/) </p>
