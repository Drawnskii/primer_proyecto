<div id="searcher" class="w-screen h-screen">
  <div class="w-full h-full flex flex-col items-center justify-center space-y-6">
    
    <!-- Título enorme -->
    <h1 class="text-5xl font-bold text-gray-800">Consulta el Clima</h1>
    
    <!-- Imagen del clima -->
    <img 
      src="https://cdn-icons-png.flaticon.com/512/1163/1163661.png" 
      alt="Clima" 
      class="w-32 h-32 object-contain" 
    />
    
    <!-- Dropdown de ciudades -->
    <select id="city-select" class="px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
      <option value="">Selecciona una ciudad</option>
      <option value="-1.2543401,-78.6228502">Ambato</option>
      <option value="-2.90055,-79.00453">Cuenca</option>
      <option value="-2.170998,-79.922359">Guayaquil</option>
      <option value="-0.9354,-78.6156">Latacunga</option>
      <option value="-0.22985,-78.52495">Quito</option>
    </select>

    <!-- Botón para navegar -->
    <a 
      href="#weather" 
      id="go-button"
      class="px-6 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition"
    >
      Ver clima
    </a>

  </div>
</div>
