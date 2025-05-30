<script>
  import Searcher from './Searcher.svelte';
  import Weather from './Weather.svelte';

  let weatherData = null;
</script>

<Searcher on:weatherLoaded={(e) => weatherData = e.detail.weatherData} />

{#if weatherData}
  <Weather {weatherData} />
{/if}
