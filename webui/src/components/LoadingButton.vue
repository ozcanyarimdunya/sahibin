<template>
  <button :class="{'disabled': loading}">
    <span class="spinner-border-sm spinner-border text-white"
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
})
</script>

<style scoped>

</style>
