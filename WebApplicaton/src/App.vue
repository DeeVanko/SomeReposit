<template>
  <div>
    <!-- Левая боковая панель -->
    <div class="leftbar">
      <!-- Ваш код для левой боковой панели -->
    </div>

    <!-- Главный контент и компонент LeftNavBar -->
    <div class="content">
      <router-view></router-view>
      <LeftNavBar></LeftNavBar>
    </div>
  </div>
</template>

<script>
import LeftNavBar from '@/components/LeftNavBar.vue';

export default {
  components: {
    LeftNavBar
  }
};
</script>

<style>
/* Стили для левой боковой панели и области контента */
.leftbar {
  width: 600px;
  background-color: #f0f0f0;
  padding: 20px;
  float: left;
}

.content {
  margin-left: 220px;
  padding: 20px;
}
</style>