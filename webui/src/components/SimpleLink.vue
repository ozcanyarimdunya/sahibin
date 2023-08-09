<template>
  <div class="code">
    <small class="me-2">{{ link }}</small>
    <span role="button">
      <i class="bi bi-clipboard" v-if="!copied" @click="onCopyLink"></i>
      <i class="bi bi-check-lg" v-else></i>
    </span>
  </div>
</template>

<script setup>
import {useClipboard} from "@/utils";

const {copy, copied} = useClipboard()

const props = defineProps({
  link: {type: String}
})
const onCopyLink = () => copy(props.link)
</script>

<style scoped>

</style>
