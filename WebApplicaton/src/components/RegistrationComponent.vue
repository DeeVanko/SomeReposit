<template>
  <div class="CONTEINER-RP">
    <img id="IMG-LOGO" :src = "require('@/assets/OdynXBET-logo.png')" alt="Logo">

    <div class="FORM-GROUP-2">
      <label class="FORM-GROUP-2-LABEL" for="USERNAME">Username:</label>
      <input class="FORM-GROUP-2-INPUT" type="text" id="USERNAME" name="USERNAME" required placeholder="AltynbekOV04">
      <div class="error-message" id="USERNAME-error"></div>
      <div class="correct-message" id="USERNAME-correct"></div>
    </div>

    <div class="FORM-GROUP-2">
      <label class="FORM-GROUP-2-LABEL" for="PASSWORD">Password:</label>
      <input class="FORM-GROUP-2-INPUT" type="password" id="PASSWORD" name="PASSWORD" required placeholder="Qwerty12345">
      <div class="error-message" id="PASSWORD-error"></div>
      <div class="correct-message" id="PASSWORD-correct"></div>
    </div>

    <div class="FORM-GROUP-2">
      <button class="FORM-GROUP-2-BUTTON" type="button" @click="registerUser()">Register</button>
    </div>

    <div class="SEPARATOR"></div>
    <router-link to="/login" class="LINK-LOGIN">Login</router-link>
  </div>
</template>


<script>
import '@/assets/JS-FOR-ALL.js';
import {registerUser} from '@/assets/JS-FOR-ALL.js';
export default {
  mounted() {
    // Вызовите функции из внешнего JavaScript-файла
    registerUser();
  },
  methods: {
    registerUser() {
      // Вызовите функцию из внешнего JavaScript-файла
      registerUser();
    }
  }
}
</script>

<style scoped>
@import '@/assets/CSS-FOR-ALL.css';
</style>
