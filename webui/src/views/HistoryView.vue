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

        <main v-if="loading">
          <p class="text-center text-secondary">Loading...</p>
        </main>
        <main v-else>
          <div class="border rounded-1 mb-3" v-for="(item, index) in items" :key="index">
            <div class="d-flex flex-column flex-sm-row align-items-center justify-content-between p-2">
              <router-link :to="{name: 'share', params: {key: item.key}}"
                           class="card-link text-decoration-none opacity-75 item-link">

                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                  <path
                      d="M4.715 6.542 3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1.002 1.002 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4.018 4.018 0 0 1-.128-1.287z"/>
                  <path
                      d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 1 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 1 0-4.243-4.243L6.586 4.672z"/>
                </svg>
                {{ url }}/share/{{ item.key }}
              </router-link>
              <small class="opacity-50 text-nowrap item-date">
                {{ formattedDate(item.timestamp) }}</small>
            </div>
            <v-ace-editor
                class="rounded-1 border-top rounded-top-0 opacity-75"
                :max-lines="item.data.split('\n').length"
                theme="chrome"
                v-model:value="item.data"
                :print-margin="false"
                readonly
                :options="{ highlightActiveLine: false }"
            />
          </div>
          <div class="text-secondary text-start mt-2 small">Showing up to 50 snippets.</div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import pasteService from "@/service";

const loading = ref(false);
let items = ref([])

const loadHistoryItems = () => {
  loading.value = true;
  pasteService
      .history()
      .then(data => items.value = data)
      .finally(() => loading.value = false)
}
onMounted(() => loadHistoryItems())
const url = window.location.origin

const formattedDate = (inputDateTime) => {
  return new Date(inputDateTime).toISOString().slice(0, 19).replace("T", " ");
}
</script>

<style scoped>
.item-link {
  font-size: .75rem;
}

.item-date {
  font-size: .75rem;
}
</style>
