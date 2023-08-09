<template>
  <div class="d-flex flex-column">
    <div class="input-group my-1">
      <input type="text" class="form-control code" :value="content" readonly>
      <button class="input-group-text btn btn-outline-secondary border d-inline-flex align-items-center"
              @click="onCopy">
        <i class="bi bi-check-lg" v-if="copied"/>
        <i class="bi bi-clipboard" v-else/>
      </button>
    </div>
    <pre class="text-bg-dark p-2 rounded-1 mt-1" v-if="output">$ {{ output }}</pre>
  </div>
</template>

<script setup>
import {useClipboard} from "@/utils";

const props = defineProps({
  content: {
    type: String
  },
  output: {
    type: String,
    default: null
  }
})

const {copy, copied} = useClipboard()

const onCopy = () => copy(props.content)

</script>

<style scoped>
</style>
