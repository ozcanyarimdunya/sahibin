<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <div class="col-12 col-lg-8 text-center mx-auto">
        <h2 class="error-heading mb-5">Oops!</h2>
        <div class="border p-5">
          <code>{{ errorMessage }}</code>
        </div>
        <router-link :to="{name: 'home'}" class="btn btn-primary mt-4">Go Back to Homepage</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import {useRoute} from "vue-router";

const route = useRoute();

const errorMessage = route.query.msg ? route.query.msg : 'Oops! The page you are looking for was not found.'
</script>

<style scoped>
body {
  background-color: #f8f9fa;
}

.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 12rem);
  text-align: center;
}

.error-heading {
  font-size: 4rem;
  font-weight: bold;
  color: #dc3545;
}

.error-message {
  font-size: 1.5rem;
  margin-top: 1rem;
  color: #555;
}
</style>
