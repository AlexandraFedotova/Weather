<h2>Описание</h2>

Веб-сервис получает данные о погоде из публичного API и производит их агрегацию, после чего возвращает результат в следующем формате: 

<pre>
{ 
 "city": "Saint-Petersburg",
 "from": "2021-10-07",
 "to": "2021-10-03",
 "temperature_c": {
   "average": 25.0,
   "median": 24.5,
   "min": 20.1,
   "max": 29.3
 },
 "humidity": {
   "average": 55.4,
   "median": 58.1,
   "min": 43.1,
   "max": 82.4
 },
 "pressure_mb": {
   "average": 1016.0,
   "median": 1016.5,
   "min": 1015.1,
   "max": 1017.3
 }
}
</pre></p>

<h2>Установление зависимостей </h2>

<p>
Для установления зависимостей выполните следующую комманду
<pre> pip install -r requirements.txt </pre>
Также, необходимо получить api-key на <a href="https://www.visualcrossing.com/">visualcrossing.com</a>
Ключ вставляется в файл .env вместо "Your_api_key"
</p>

<h2>Использование</h2> 

<p>
Корректный формат запроса к сервису: <pre>GET /weather?city=&ltcity>&days=&ltn></pre>
Например, GET /weather?city=Saint-Petersburg&days=4 

Для запуска приложения из консоли:

<pre>cd Weather
run flask</pre>

</p> 

<h2> Docker </h2>
  <p> Для построения Docker image
 
    docker build -t weather '[full path to Dockerfile]'
    docker run -p 8080:5000 --name weather --env-file=.env weather 

  Или Вы можете скачать Docker image: 
  
    docker pull alexandrafedotova/weather 
    docker run -p 8080:5000 --name weather --env-file=.env alexandrafedotova/weather

  Сервис работает на: localhost:8080
  </p>
  
<h2> Jenkins </h2>
