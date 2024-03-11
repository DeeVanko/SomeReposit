// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginComponent from '@/components/LoginComponent.vue';
import RegistrationComponent from '@/components/RegistrationComponent.vue';

const routes = [
  { path: '/login', component: LoginComponent },
  { path: '/registration', component: RegistrationComponent },
  // Другие маршруты, если необходимо
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;