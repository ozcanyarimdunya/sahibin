<template>
  <div class="container-lg">
    <div class="row">
      <div class="col-12">
        <div class="d-flex align-items-center justify-content-between gap-2 py-3">
          <loading-button class="btn btn-sm btn-outline-dark rounded-1 px-3"
                          :loading="loading.download"
                          @click="onDownload"
                          v-show="!error">
            Download
          </loading-button>
          <button class="btn btn-sm btn-primary rounded-1 px-3"
                  @click="onCopyShareableURL"
                          v-show="!error">
            <span v-if="copied4URL">Copied!</span>
            <span v-else>Copy Shareable URL</span>
          </button>
        </div>
      </div>
      <div class="col-12">
        <v-ace-editor
            class="border rounded-1 ace-editor"
            theme="chrome"
            readonly
            v-model:value="editor"
            :print-margin="false"
        />
        <div class="position-relative" v-show="!error">
          <button class="btn btn-primary btn-floating position-absolute float-end shadow rounded-circle"
                  @click="onCopyEditorContent">
            <svg v-if="copied4Content" width="32" height="32" viewBox="0 0 24 24" fill="none"
                 xmlns="http://www.w3.org/2000/svg">
              <path d="M4 12L10 18L20 6" stroke="white" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round"/>
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512">
              <rect x="128" y="128" width="336" height="336" rx="57" ry="57" fill="none" stroke="#FFF"
                    stroke-linecap="round" stroke-linejoin="round" stroke-width="32px"/>
              <path
                  d="M383.5,128l.5-24a56.16,56.16,0,0,0-56-56H112a64.19,64.19,0,0,0-64,64V328a56.16,56.16,0,0,0,56,56h24"
                  fill="none" stroke="#FFF" stroke-linecap="round" stroke-linejoin="round" stroke-width="32px"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted, reactive, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import {setupBootstrap} from "@/plugins";
import pasteService from "@/service";
import LoadingButton from "@/components/LoadingButton.vue";
import {useClipboard} from "@/utils";

const route = useRoute()
const router = useRouter()
const editor = ref('')
const error = ref(false)

const loading = reactive({editor: false, download: false});
const {copy: copy4Content, copied: copied4Content} = useClipboard()
const {copy: copy4URL, copied: copied4URL} = useClipboard()

const onCopyShareableURL = () => copy4URL(window.location.origin + route.fullPath);
const onCopyEditorContent = () => copy4Content(editor.value)

const loadEditorContent = () => {
  loading.editor = true
  pasteService
      .get(route.params.key)
      .then(data => editor.value = data.data)
      .catch(() => {
        error.value = true;
        editor.value = "We're sorry, but the contents of the paste could not be found, or it has been expired."
      })
      .finally(() => loading.editor = false)
}

const onDownload = () => {
  loading.download = true
  const filename = `${route.params.key}.txt`;
  const blob = new Blob([editor.value], {type: 'text/plain'});
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click()
  URL.revokeObjectURL(url)
  loading.download = false
}

onMounted(() => {
  setupBootstrap()
  loadEditorContent()
})

</script>


<style scoped>
.ace-editor {
  height: calc(100vh - 9rem);
}

.btn-floating {
  height: 4rem;
  width: 4rem;
  bottom: 2rem;
  right: 2rem;
}

@media (max-width: 575px) {
  .ace-editor {
    height: calc(100vh - 9rem);
  }
}
</style>
