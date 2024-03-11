// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

createApp(App)
  .use(router) // Используйте роутер в экземпляре Vue
  .mount('#app');