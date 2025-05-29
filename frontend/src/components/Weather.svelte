<div id="weather" class="w-screen h-screen bg-eggplant-700 p-16 flex items-center">
  <div class="w-full rounded-xl shadow-lg bg-eggplant-600 text-white p-10 flex flex-col space-y-8">

    <!-- Título -->
    <h2 class="text-4xl font-bold">Datos del Clima</h2>

    <!-- Información del clima -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

      <!-- Ciudad y clima principal -->
      <div class="flex items-center space-x-6">
        <img 
          src="https://openweathermap.org/img/wn/04d@2x.png" 
          alt="Icono del clima" 
          class="w-20 h-20"
        />
        <div>
          <h3 class="text-2xl font-semibold">Ciudad: <span class="font-normal">Texarkana</span></h3>
          <p class="text-lg">Descripción: <span class="font-normal">broken clouds</span></p>
        </div>
      </div>

      <!-- Detalles del clima -->
      <div class="text-lg space-y-2">
        <p>🌡️ Temperatura: <span class="font-semibold">19.4 °C</span></p>
        <p>🤗 Sensación térmica: <span class="font-semibold">19.7 °C</span></p>
        <p>💧 Humedad: <span class="font-semibold">89%</span></p>
        <p>🌬️ Viento: <span class="font-semibold">3.13 m/s</span></p>
      </div>
    </div>

    <!-- Alerta meteorológica (si existe) -->
    <div class="bg-red-600 bg-opacity-80 p-4 rounded-lg shadow">
      <h4 class="text-xl font-bold mb-2">⚠️ Alerta: Small Craft Advisory</h4>
      <p class="text-sm whitespace-pre-line">
        ...SMALL CRAFT ADVISORY REMAINS IN EFFECT FROM 5 PM THIS
        AFTERNOON TO 3 AM EST FRIDAY...
        * WHAT...North winds 15 to 20 kt with gusts up to 25 kt and seas
        3 to 5 ft expected.
        * WHERE...Coastal waters from Little Egg Inlet to Great Egg
        Inlet NJ out 20 nm...
      </p>
    </div>

  </div>
</div>
