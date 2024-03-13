<template>
  <div class="CONTEINER-LP">
    <img id="IMG-LOGO" :src = "require('@/assets/OdynXBET-logo.png')" alt="Logo">

    <div class="FORM-GROUP-1">
      <label class="FORM-GROUP-1-LABEL" for="USERNAME">Username:</label>
      <input class="FORM-GROUP-1-INPUT" type="text" id="USERNAME" name="USERNAME" required placeholder="AltynbekOV04">
      <div class="error-message" id="USERNAME-error"></div>
      <div class="correct-message" id="USERNAME-correct"></div>
    </div>

    <div class="FORM-GROUP-1">
      <label class="FORM-GROUP-1-LABEL" for="PASSWORD">Password:</label>
      <input class="FORM-GROUP-1-INPUT" type="password" id="PASSWORD" name="PASSWORD" required placeholder="Qwerty12345">
      <div class="error-message" id="PASSWORD-error"></div>
      <div class="correct-message" id="PASSWORD-correct"></div>
    </div>

    <div class="FORM-GROUP-1">
      <router-link to="/Main" class="LINK-FORGOT-PASSWORD">Forgot Password</router-link>
    </div>

    <div class="FORM-GROUP-1">
      <button class="FORM-GROUP-1-BUTTON" type="button" @click="loginUser()">Login</button>
    </div>

    <div class="SEPARATOR"></div>
    <router-link to="/registration" class="LINK-REGISTER">Register</router-link>
  </div>
</template>


<script>
import '@/assets/JS-FOR-ALL.js';
import {loginUser} from '@/assets/JS-FOR-ALL.js';
export default {
  mounted() {
    // Вызовите функции из внешнего JavaScript-файла
    loginUser();
  },
  methods: {
    loginUser() {
      // Вызовите функцию из внешнего JavaScript-файла
      loginUser();
    }
  }
}
</script>

<style scoped>
@import '@/assets/CSS-FOR-ALL.css';
</style>
