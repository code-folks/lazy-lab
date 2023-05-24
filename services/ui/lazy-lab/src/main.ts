import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router  from './router';
import { appStore } from './stores';

const app = createApp(App);

app.use(router);
app.use(appStore);
app.mount('#app');
