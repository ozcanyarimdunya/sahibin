<template>
  <button :class="{'disabled': loading}">
    <span class="spinner-border-sm spinner-border"
          :class="spinnerClass"
          role="status"
          v-if="loading"/>
    <slot/>
  </button>
</template>
<script setup>
defineProps({
  loading: {
    type: Boolean,
    default: false
  },
  spinnerClass: {
    type: String,
    default: 'text-white'
  }
})
</script>

<style scoped>

</style>
