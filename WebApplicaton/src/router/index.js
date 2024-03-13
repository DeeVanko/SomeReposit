// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginComponent from '@/components/LoginComponent.vue';
import RegistrationComponent from '@/components/RegistrationComponent.vue';
import LeftNavBar from '@/components/LeftNavBar.vue';

const routes = [
  { path: '/main', component: LeftNavBar },
  { path: '/login', component: LoginComponent },
  { path: '/registration', component: RegistrationComponent },
  // Другие маршруты, если необходимо

  { path: '/I', component: RegistrationComponent },
  { path: '/II', component: RegistrationComponent },
  { path: '/III', component: RegistrationComponent },
  { path: '/IIII', component: RegistrationComponent },
  { path: '/IIIII', component: RegistrationComponent },
  { path: '/IIIIII', component: RegistrationComponent },
  { path: '/IIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIIIIIIII', component: RegistrationComponent },
  { path: '/IIIIIIIIIIIIIIII', component: RegistrationComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;