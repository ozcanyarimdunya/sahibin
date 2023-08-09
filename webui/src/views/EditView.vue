<template>
  <div class="container-lg">
    <div class="row">
      <div class="col-12">
        <div class="py-3 d-flex align-items-center gap-3">
          <div class="w-75 position-relative">
            <input v-model="title"
                   class="form-control form-control-sm input-title"
                   type="text"
                   maxlength="50"
                   placeholder="Paste title (optional)"/>
            <small class="position-absolute text-secondary fw-light countdown" v-if="title.length>0">
              {{ title.length }}/50
            </small>
          </div>
          <div class="d-flex column-gap-3 flex-row w-auto">
            <select class="form-select form-select-sm text-center" v-model="expire" :disabled="loading">
              <option selected value="1">Expire in one day</option>
              <option value="7">Expire in one week</option>
              <option value="30">Expire in one month</option>
              <option value="-1">Never expire</option>
            </select>
            <loading-button
                class="btn btn-sm btn-outline-primary rounded-1 px-3 text-nowrap"
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
import {onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import LoadingButton from "@/components/LoadingButton.vue";
import pasteService from "@/service";
import {safeString} from "@/utils";

const route = useRoute()
const router = useRouter()
const loading = ref(false);
const editor = ref('')
const timestamp = ref('')
const expire = ref(1)
const title = ref('')

const loadPaste = () => {
  editor.value = "loading ..."
  pasteService
      .get(route.params.key)
      .then(({data}) => {
        editor.value = data.data;
        expire.value = data.expire <= 0 ? -1 : data.expire;
        title.value = safeString(data.title, '')
        timestamp.value = data.timestamp
      })
      .catch((err) => editor.value = `We're sorry, but the you're not authorized to edit the paste content.\nError: ${err}`)
}

const onSave = () => {
  loading.value = true
  pasteService
      .edit(route.params.key, {data: editor.value, expire: expire.value, title: title.value.substring(0, 50)})
      .then(({data}) => router.push({name: 'share', params: {key: data.key}}))
      .catch(err => console.warn(err))
      .finally(() => loading.value = false)
}

onMounted(() => loadPaste())
</script>

<style scoped>
.ace-editor {
  height: calc(100vh - 9rem);
}

.countdown {
  right: 1%;
  font-size: .75rem;
  top: 22.5%
}

.input-title::placeholder {
  --bs-text-opacity: 1;
  font-weight: 300 !important;
  color: rgba(var(--bs-secondary-rgb), var(--bs-text-opacity)) !important;
}
</style>
