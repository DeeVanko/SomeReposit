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
      <a class="LINK-FORGOT-PASSWORD" href="NAVBAR.html">Forgot Password</a>
    </div>

    <div class="FORM-GROUP-1">
      <button class="FORM-GROUP-1-BUTTON" type="button" onclick="loginUser()">Login</button>
    </div>

    <div class="SEPARATOR"></div>
    <a class="LINK-REGISTER" href="Registration.html">Register</a>
  </div>
</template>


<script>
export default {
  methods: {
    loginUser() {
      // Ваша логика для обработки входа пользователя
    }
  }
}
</script>

<style scoped>
@import './CSS-FOR-ALL.css';
</style>
