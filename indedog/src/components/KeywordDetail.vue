<template>
    Keyword
    <button
    type="button"
    class="btn btn-link"
      ref="targetElement"
      @click="visible = !visible"
    >
       . 
    </button>
  
    <Wowerlay
      tag="section"
      :target="targetElement"
      v-model:visible="visible"
      style="background-color: aliceblue;"
    >
      <div v-for="keyword in props.keywordList">
        <p @click="goResult(keyword)" style="text-decoration: none; margin-bottom: 0;">
            #{{ keyword }}
        </p>
      </div>
    </Wowerlay>
  </template>
  
  <script setup lang="ts">
    import { Wowerlay } from 'wowerlay';
    import { ref, computed } from 'vue';
    import { useCounterStore } from '@/stores/counter'
    import { useRouter } from 'vue-router'
  
    const targetElement = ref<HTMLElement>();
    const visible = ref(false);
    const router = useRouter()

    const goResult = function(keyword) {
      router.push({ name: 'movie_search_result', params: { 'category': '키워드', 'name': keyword}})
      .then(() => {
        window.location.reload()});
    }

    const props = defineProps({
        keywordList: Object
    })
    
  </script>

<style scoped>
@import '@/assets/font/font.css';

* {
    font-family: "hanna_air"
}
</style>