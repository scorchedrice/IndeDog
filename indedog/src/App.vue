<template>
  <div>
    <div style="text-align: center; margin-top: 20px;">
      <RouterLink :to="{name: 'home'}">
        <img src="@/assets/icon/site_icon_1.jpg" class="rounded col" alt="Home" width="100px" height="100px">
      </RouterLink>
    </div>
  <br>
  <div class="container" style="width: 1200px;">
    <div class="row">
        <div>
          <RouterView />
          <Menu />
        </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import Menu from '@/components/Menu.vue'
</script>

<style scoped>

</style>