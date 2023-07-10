<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 py-3 d-flex justify-content-end flex-column flex-sm-row">
        <loading-button
            class="btn btn-sm btn-primary rounded-1 px-5"
            :loading="loading"
            :class="{'disabled': !editor || loading}"
            @click="onSave">
          Save
        </loading-button>
      </div>
      <div class="col-12">
        <v-ace-editor
            class="border rounded-1 ace-editor"
            theme="chrome"
            v-model:value="editor"
            :print-margin="false"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue";
import {useRouter} from "vue-router";
import LoadingButton from "@/components/LoadingButton.vue";
import pasteService from "@/service";

const router = useRouter()
const loading = ref(false);
const editor = ref('')


const onSave = () => {
  loading.value = true
  pasteService
      .create(editor.value)
      .then(data => router.push({name: 'share', query: {key: data.key}}))
      .catch(err => console.warn(err))
      .finally(() => loading.value = false)
}

</script>


<style scoped>
.ace-editor {
  height: calc(100vh - 10rem);
}
</style>
