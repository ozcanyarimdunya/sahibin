<template>
  <div class="container-lg">

    <div class="row">
      <div class="col-12">
        <div class="mt-2 mt-sm-3 border rounded-1">
          <div class="d-flex flex-column flex-md-row align-items-start justify-content-between p-3">
            <div class="d-flex flex-column gap-2">
              <span class="text-dark">{{ title }}</span>
              <div style="font-size: .8rem" class="d-flex align-items-center gap-2">
                <small class="text-secondary d-inline-flex align-items-center gap-1">
                  <i class="bi bi-clock"></i>
                  <span>{{ createdTime }}</span>
                </small>
                <small class="text-secondary d-inline-flex align-items-center gap-1 border-start ps-2">
                  <i class="bi bi-eye"></i>
                  <span>{{ views + 1 }}</span>
                </small>
                <small class="text-secondary d-inline-flex align-items-center gap-1 border-start ps-2">
                  <i class="bi bi-download" v-if="!loading.download"></i>
                  <i class="spinner-border-sm spinner-border" role="status" v-else></i>
                  <span role="button"
                        class="link-subtitle"
                        @click="onDownload">
                    Download
                  </span>
                </small>
                <small class="text-primary d-inline-flex align-items-center gap-1 border-start ps-2" v-if="isAuthor">
                  <i class="bi bi-pencil"></i>
                  <span role="button"
                        class="link-subtitle"
                        @click="onEdit">
                    Edit
                  </span>
                </small>
                <small class="text-danger d-inline-flex align-items-center gap-1 border-start ps-2" v-if="!deleteItem && isAuthor">
                  <i class="bi bi-trash"></i>
                  <span role="button"
                        class="link-subtitle"
                        @click="onPreDelete">
                    Delete
                  </span>
                </small>
                <small class="text-danger d-inline-flex align-items-center gap-1 border-start ps-2" v-else-if="isAuthor">
                  <i class="bi bi-check-lg"></i>
                  <span role="button"
                        class="link-subtitle"
                        @click="onDelete">
                    Confirm
                  </span>
                </small>
              </div>
            </div>
            <div class="d-flex align-items-center gap-2 mt-1 mt-sm-0">
              <simple-link :link="shareableURL"/>
            </div>
          </div>
          <div>
            <v-ace-editor
                class="border-top ace-editor"
                theme="chrome"
                readonly
                v-model:value="editor"
                :print-margin="false"
                :options="{
                highlightActiveLine: false,
            }"
            />
            <div class="position-relative" v-show="!error">
              <button class="btn btn-primary btn-floating position-absolute float-end shadow rounded-circle"
                      :class="{'disabled': loading.editor}"
                      @click="onCopyEditorContent">
                <i class="bi bi-check-lg fs-3" v-if="copied"></i>
                <i class="bi bi-clipboard fs-3" v-else></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {computed, onMounted, reactive, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import {formatDatetime, safeString, useClipboard, useCookie} from "@/utils";
import pasteService from "@/service";
import SimpleLink from "@/components/SimpleLink.vue";

const cookie = useCookie()
const {copy, copied} = useClipboard()
const route = useRoute()
const router = useRouter()

const editor = ref('')
const title = ref('')
const views = ref(0)
const error = ref(false)
const timestamp = ref('')
const loading = reactive({editor: false, download: false});
const shareableURL = computed(() => window.location.origin + route.fullPath)
const createdTime = computed(() => formatDatetime(timestamp.value))
const deleteItem = ref(false)
const isAuthor = ref(false)

const onCopyEditorContent = () => copy(editor.value)
const loadEditorContent = () => {
  loading.editor = true;
  editor.value = "loading ..."
  pasteService
      .get(route.params.key)
      .then(({data, headers}) => {
        editor.value = data.data;
        title.value = safeString(data.title, '(No title)')
        timestamp.value = data.timestamp
        views.value = data.views || 0
        isAuthor.value = cookie.get("user-session-id") === headers.get("user-session-id")
      })
      .catch((err) => {
        error.value = true;
        editor.value = `We're sorry, but the contents of the paste could not be found, or it has been expired.\nError: ${err}`
      })
      .finally(() => loading.editor = false)
}
const onDownload = () => {
  loading.download = true
  const filename = `${route.params.key}.txt`;
  const blob = new Blob([editor.value], {type: 'text/plain'});
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click()
  URL.revokeObjectURL(url)
  loading.download = false;
}
const onEdit = () => router.push({name: 'edit', params: {key: route.params.key}})
const onPreDelete = () => {
  deleteItem.value = true;
  setTimeout(() => deleteItem.value = false, 1500)
}
const onDelete = () => {
  pasteService
      .delete(route.params.key)
      .then(() => router.push({name: 'home'}))
      .catch((err) => console.warn(err))
}

onMounted(() => loadEditorContent())

</script>


<style scoped>
.ace-editor {
  height: calc(100vh - 11rem);
}

.btn-floating {
  height: 4rem;
  width: 4rem;
  bottom: 2rem;
  right: 1rem;
}

.link-subtitle:hover {
  text-decoration: underline;
}

@media (max-width: 575px) {
  .ace-editor {
    height: calc(100vh - 12rem);
  }

  .code {
    font-size: .8em;
  }
}
</style>
