<template>
  <div class="container-lg">
    <div class="row">
      <div class="col-12 mx-auto py-4">
        <header class="d-flex align-items-center pb-3 mb-5 border-bottom text-center flex-column fw-bold">
          <h1>History</h1>
          <p class="text-secondary fw-light">
            Your Past Text and Code Snippets!
          </p>
        </header>
        <div class="d-flex align-items-center justify-content-end mb-4 gap-1 col-12 col-md-6 mx-auto">
          <div class="position-relative w-100">
            <input class="form-control form-control-sm"
                   type="text"
                   placeholder="Type to search..."
                   v-model="searchKey"
                   @change="onSearch">
            <button class="position-absolute btn btn-sm btn-outline-dark border rounded-start-0 btn-search"
                    @click="onSearch">
              <i class="bi bi-search"></i>
            </button>
          </div>
          <button class="btn btn-sm btn-outline-dark border"
                  data-bs-toggle="tooltip"
                  data-bs-title="Export All Pastes"
                  @click="onExport">
            <i class="bi bi-cloud-download" v-if="!exportLoading"></i>
            <span class="spinner-border spinner-border-sm text-secondary" v-else></span>
          </button>
        </div>

        <main v-if="loading">
          <p class="text-center text-secondary">Loading...</p>
        </main>
        <main v-else>
          <div class="border rounded-1 mb-4" v-for="(item, index) in items" :key="index">
            <div
                class="d-flex flex-column flex-sm-row align-items-start align-items-sm-center justify-content-between p-2 bg-gradient bg-body-tertiary">
              <router-link :to="{name: 'share', params: {key: item.key}}"
                           class="card-link text-decoration-none d-inline-flex align-items-center gap-1 small">
                {{ safeString(item.title, `${url}/share/${item.key}`) }}
              </router-link>
              <small class="text-nowrap d-flex align-items-center justify-content-between gap-2">
                <small class="d-inline-flex align-items-center gap-1 border-end pe-2">
                  <i class="bi bi-clock"></i>
                  <span>{{ formatDatetime(item.timestamp) }}</span>
                </small>
                <small class="d-flex align-items-center gap-1 border-end pe-2">
                  <i class="bi bi-eye"></i>
                  <span>{{ item.views ? item.views : 1 }}</span>
                </small>
                <span v-if="!deleteItems[item.key]" role="button" class="text-danger" @click="confirm4Delete(item)">
                  <i class="bi bi-trash fs-6"></i>
                </span>
                <span v-else role="button" class="text-danger" @click="deleteItem(item)">
                  <i class="bi bi-check-lg fs-6"></i>
                </span>
              </small>
            </div>
            <v-ace-editor
                readonly
                theme="chrome"
                class="rounded-1 border-top rounded-top-0 opacity-75"
                v-model:value="item.data"
                :max-lines="item.data.split('\n').length"
                :print-margin="false"
                :options="{ highlightActiveLine: false }"
            />
          </div>
          <div class="text-secondary text-center mb-2" v-if="!items.length">No paste found.</div>
          <div class="text-secondary text-start mt-2 small" v-else>Showing up to 50 snippets.</div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import pasteService from "@/service";
import {formatDatetime, safeString} from "@/utils";

const loading = ref(false);
let items = ref([])
const url = window.location.origin
const deleteItems = ref({})
const searchKey = ref('')
const exportLoading = ref(false)

const loadHistoryItems = (q = '') => {
  loading.value = true;
  pasteService
      .history(q)
      .then(({data}) => {
        items.value = data;
        const deleteObj = {};
        data.forEach(it => deleteObj[it.key] = false)
        deleteItems.value = deleteObj
      })
      .finally(() => loading.value = false)
}

const deleteItem = (item) => {
  pasteService
      .delete(item.key)
      .then(() => items.value = items.value.filter(it => it.key !== item.key))
}

const confirm4Delete = (item) => {
  deleteItems.value[item.key] = true
  setTimeout(() => deleteItems.value[item.key] = false, 1500)
}

const onSearch = () => {
  loadHistoryItems(searchKey.value)
}
const onExport = () => {
  exportLoading.value = true
  pasteService
      .export()
      .then(({data}) => {
        const blob = new Blob([data], {type: 'application/zip'});
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob)
        link.download = `export-${new Date().getTime()}.zip`
        link.click()
      })
      .catch(err => console.warn(err))
      .finally(() => exportLoading.value = false)
}

onMounted(() => loadHistoryItems())
</script>

<style scoped>
.btn-search {
  right: 0;
  top: 0
}
</style>
