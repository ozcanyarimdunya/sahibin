import {createApp} from 'vue'

import App from '@/App.vue'
import router from '@/router'
import '@/assets/styles.scss'
import 'bootstrap-icons/font/bootstrap-icons.css'
import {setupAceEditor, setupBootstrap} from "@/plugins";
import {VAceEditor} from "vue3-ace-editor";

setupAceEditor()
createApp(App)
    .use(router)
    .component('VAceEditor', VAceEditor)
    .mount('#app');
setupBootstrap()
