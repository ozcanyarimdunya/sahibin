<template>
  <div class="container-lg">
    <div class="row">
      <div class="col-12">
        <div class="py-3 d-flex justify-content-end flex-column flex-sm-row gap-3">
          <div class="d-flex column-gap-3">
            <select class="form-select form-select-sm" v-model="expire" :disabled="loading">
              <option selected value="1">Expire in one day</option>
              <option value="7">Expire in one week</option>
              <option value="30">Expire in one month</option>
              <option value="-1">Never expire</option>
            </select>
            <loading-button
                class="btn btn-sm btn-primary rounded-1 px-3 text-nowrap"
                :loading="loading"
                :class="{'disabled': !editor || loading}"
                @click="onSave">
              Save Paste
            </loading-button>
          </div>
        </div>
      </div>
      <div class="col-12">
        <v-ace-editor
            class="border rounded-1 ace-editor"
            theme="chrome"
            v-model:value="editor"
            :print-margin="false"
            :options="{
                highlightActiveLine: false,
            }"
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
const expire = ref(1)

const onSave = () => {
  loading.value = true
  pasteService
      .create({data: editor.value, expire: expire.value})
      .then(data => router.push({name: 'share', params: {key: data.key}}))
      .catch(err => console.warn(err))
      .finally(() => loading.value = false)
}
</script>

<style scoped>
.ace-editor {
  height: calc(100vh - 9rem);
}
</style>
