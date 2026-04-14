<template>
  <div>
    <div v-for="movie in movies" :key="movie.id">
      <img :src="movie.poster" width="200" />
      <h3>{{ movie.title }}</h3>
      <p>{{ movie.description }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then(res => res.json())
    .then(data => {
      movies.value = data.movies;
    });
}

onMounted(() => {
  fetchMovies();
});
</script>