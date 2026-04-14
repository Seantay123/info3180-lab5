<template>
  <form id="movieForm" @submit.prevent="saveMovie">
    
    <div>
      <label>Title</label>
      <input type="text" name="title" />
    </div>

    <div>
      <label>Description</label>
      <textarea name="description"></textarea>
    </div>

    <div>
      <label>Poster</label>
      <input type="file" name="poster" />
    </div>

    <button type="submit">Submit</button>

  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(res => res.json())
    .then(data => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err));
}

onMounted(() => {
  getCsrfToken();
});
</script>