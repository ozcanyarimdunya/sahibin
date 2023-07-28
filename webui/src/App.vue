<template>
  <div>
    <app-header/>
    <router-view/>
  </div>
</template>

<script setup>
import AppHeader from "@/components/AppHeader.vue";
import {onBeforeMount, onMounted} from "vue";
import {setupBootstrap} from "@/plugins";
import {generateRandomString, useCookie} from "@/utils";
import axios from "axios";

const {get, set} = useCookie()

onBeforeMount(() => {
  const sessionid = get('user-session-id');
  if (!sessionid) {
    set('user-session-id', generateRandomString(24), 365)
  }
  axios.defaults.headers.common["user-session-id"] = sessionid;
})

onMounted(() => setupBootstrap())

</script>

<style scoped>
</style>
