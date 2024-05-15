<template>
  <div id="app">
    <div style="text-align: center; margin-top: 20px;">
      <h1 id="HomePage" @click="goHomePage">인디독</h1>
    </div>
    <br>
    <div class="container-sm" style="width: 90%;">
      <div>
        <RouterView />
        <div id="menu">
          <Menu />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router';
import Menu from '@/components/Menu.vue'
import router from './router';
const route = useRouter()
const goHomePage = function () {
  console.log('HomePage')
  route.push({name: 'home'})
}

const menuHide = function () {
  console.log('수신')
}
</script>
<style scoped>
@import '@/assets/font/font.css';
#HomePage {
  font-family: 'euljiro';
}
</style>