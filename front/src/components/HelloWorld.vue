<script setup lang="ts">
import axios from "axios";
import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
axios.get("/api/index.json").then((data)=>{
  console.log(data)
})
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
