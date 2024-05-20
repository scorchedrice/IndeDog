<template>
  <div id="app">
    <div style="text-align: center; margin-top: 20px;">
      <h1 id="HomePage" @click="goHomePage">인디독</h1>
      <Subtitle/> 
    </div>
    <br>
    <div class="container-sm" style="width: 80%;">
      <div>
        <RouterView />
        <div id="menu" style="z-index: 99; position: relative;">
          <Menu />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, routerKey, useRoute, useRouter } from 'vue-router';
import Menu from '@/components/Menu.vue'
import router from './router';
import Subtitle from '@/components/slide/MarqueeSubtitle.vue'

const route = useRouter()
const goHomePage = function () {
  route.push({name: 'home'}).then(() => {
    window.location.reload();
    // menu 에 회원가입 이후 반영이 안되는 문제 해결, home page이동시에만 새로고침 활용
  })
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