<script setup>
import { ref } from 'vue'

const title = ref('')
const description = ref('')
const posterFile = ref(null)

const handleFileUpload = (event) => {
  posterFile.value = event.target.files[0]
}

const submitMovie = async () => {
  const formData = new FormData()

  formData.append('title', title.value)
  formData.append('description', description.value)
  formData.append('poster', posterFile.value)

  const response = await fetch('http://127.0.0.1:5000/api/v1/movies', {
    method: 'POST',
    body: formData
  })

  const data = await response.json()
  console.log(data)

  // optional reset
  title.value = ''
  description.value = ''
  posterFile.value = null
}
</script>

<template>
  <form @submit.prevent="submitMovie">

    <div>
      <input v-model="title" placeholder="Title" required />
    </div>

    <div>
      <textarea v-model="description" placeholder="Description" required></textarea>
    </div>

    <div>
      <input type="file" @change="handleFileUpload" required />
    </div>

    <button type="submit">Submit</button>

  </form>
</template>