<script>
  export let weatherData;

  const kelvinToCelsius = (k) => (k - 273.15).toFixed(1);
</script>

<div id="weather" class="w-screen h-screen bg-eggplant-700 p-16 flex items-center">
  <div class="w-full rounded-xl shadow-lg bg-eggplant-600 text-white p-10 flex flex-col space-y-8">

    <!-- Título -->
    <h2 class="text-4xl font-bold">Datos del Clima</h2>

    <!-- Información del clima -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

      <!-- Ciudad y clima principal -->
      <div class="flex items-center space-x-6">
        <img 
          src={`https://openweathermap.org/img/wn/${weatherData.weather[0].icon}@2x.png`} 
          alt="Icono del clima" 
          class="w-20 h-20"
        />
        <div>
          <h3 class="text-2xl font-semibold">
            Ciudad: <span class="font-normal">{weatherData.name}</span>
          </h3>
          <p class="text-lg">
            Descripción: <span class="font-normal">{weatherData.weather[0].description}</span>
          </p>
        </div>
      </div>

      <!-- Detalles del clima -->
      <div class="text-lg space-y-2">
        <p>🌡️ Temperatura: <span class="font-semibold">{kelvinToCelsius(weatherData.main.temp)} °C</span></p>
        <p>🤗 Sensación térmica: <span class="font-semibold">{kelvinToCelsius(weatherData.main.feels_like)} °C</span></p>
        <p>💧 Humedad: <span class="font-semibold">{weatherData.main.humidity}%</span></p>
        <p>🌬️ Viento: <span class="font-semibold">{weatherData.wind.speed} m/s</span></p>
      </div>
    </div>

    {#if weatherData.alert}
    <!-- Alerta meteorológica (si existe) -->
    <div class="bg-red-600 bg-opacity-80 p-4 rounded-lg shadow">
      <h4 class="text-xl font-bold mb-2">⚠️ Alerta: {weatherData.alert.title}</h4>
      <p class="text-sm whitespace-pre-line">{weatherData.alert.description}</p>
    </div>
    {/if}

  </div>
</div>
