<template>
  <div v-if="store.isLoading">
    로딩중...
  </div>
  <div v-else id="app">
    <div style="text-align: center; margin-top: 20px;">
      <h1 id="HomePage" @click.prevent="goHomePage">인디독</h1>
      <Subtitle/> 
    </div>
    <br>
    <div class="container-sm" style="width: 90%;">
      <div>
        <RouterView />
        <div id="menu" style="z-index: 50; position: relative;">
          <Menu />
        </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, routerKey, useRoute, useRouter } from 'vue-router';
import { useCounterStore } from './stores/counter';
import Menu from '@/components/Menu.vue'
import router from './router';
import Subtitle from '@/components/slide/MarqueeSubtitle.vue'

const store = useCounterStore()
const route = useRouter()
const goHomePage = function () {
  route.push({name: 'home'})
}

const menuHide = function () {
  console.log('수신')
}
</script>
<style scoped>
@import '/node_modules/flowbite-vue/dist/index.css';
@import '@/assets/font/font.css';
#HomePage {
  font-family: 'euljiro';
}
h1, h2 {
 font-family: 'hanna' 
}
h3, h4, h5, h6, p, button, div {
  font-family: 'hanna_air'
}
</style>