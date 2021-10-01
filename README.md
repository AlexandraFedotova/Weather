<h1>Weather </h1>

<h1>Weather </h1>

<p> Веб-сервис получает данные о погоде из публичного API и производит их агрегацию, после чего возвращает результат</p>

<h2>Установление зависимостей </h2>
<p> pip install -r requirements.txt </p>

<p> Необходимо получить api_key - api.openweathermap </p>

<p> Корректный формат запроса к сервису: GET /weather?city=<city>&days=<n>. Например, GET /weather?city=Saint-Petersburg&days=4 </p> 

<h2> Docker </h2>
  <p> Для построения Docker image </p>
  <p>    
    
    docker built -t weather '[full path to Dockerfile]'
    
    docker run -p 8080:5000 --name weather --env-file=.env weather 
  </p>
  <p> Или Вы можете скачать Docker image </p>
  <p>
    
    docker pull alexandrafedotova/weather 
    
    docker run -p 8080:5000 --name weather --env-file=.env alexandrafedotova/weather
  </p>
  <p>
    Сервис работает на: 
    
    localhost:8080
  </p>
  
 
