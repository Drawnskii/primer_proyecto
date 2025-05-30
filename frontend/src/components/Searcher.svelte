<script>
  import { PUBLIC_OPEN_WEATHER_APP_API, PUBLIC_BACKEND_URL } from '$env/static/public';
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();
  let selectedCoords = '';

  const handleClick = async () => {
    if (!selectedCoords) return;

    const [lat, lon] = selectedCoords.split(',');

    try {
      const res = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${PUBLIC_OPEN_WEATHER_APP_API}`
      );

      if (res.ok) {
        const weatherData = await res.json();

        // Intentar hacer POST al backend, pero si falla solo mostrar el error en consola
        fetch(`${PUBLIC_BACKEND_URL}/weather`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ data: weatherData })
        })
          .then(async (postRes) => {
            if (!postRes.ok) {
              console.error('Error al guardar en el backend:', await postRes.text());
            }
          })
          .catch((err) => {
            console.error('No se pudo conectar al backend:', err);
          });

        // Emitimos evento personalizado con los datos
        dispatch('weatherLoaded', { weatherData });

        // Hacemos scroll hacia el div con id="weather"
        const weatherSection = document.getElementById('weather');
        if (weatherSection) {
          weatherSection.scrollIntoView({ behavior: 'smooth' });
        }
      } else {
        console.error('Error al obtener los datos del clima');
      }
    } catch (error) {
      console.error('Fallo de red:', error);
    }
  };
</script>


<div id="searcher" class="w-screen h-screen">
  <div class="w-full h-full flex flex-col items-center justify-center space-y-6">
    
    <!-- Título -->
    <h1 class="text-5xl font-bold text-gray-800">Consulta el Clima</h1>
    
    <!-- Imagen -->
    <img 
      src="https://cdn-icons-png.flaticon.com/512/1163/1163661.png" 
      alt="Clima" 
      class="w-32 h-32 object-contain" 
    />
    
    <!-- Selector -->
    <select 
      id="city-select" 
      bind:value={selectedCoords}
      class="px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    >
      <option value="">Selecciona una ciudad</option>
      <option value="-1.2543401,-78.6228502">Ambato</option>
      <option value="-2.90055,-79.00453">Cuenca</option>
      <option value="-2.170998,-79.922359">Guayaquil</option>
      <option value="-0.9354,-78.6156">Latacunga</option>
      <option value="-0.22985,-78.52495">Quito</option>
    </select>

    <!-- Botón -->
    <button 
      on:click={handleClick}
      class="px-6 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition"
    >
      Ver clima
    </button>

  </div>
</div>
