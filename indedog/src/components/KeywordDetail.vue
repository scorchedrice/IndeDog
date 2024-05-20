<template>
    <button
    type="button"
    class="btn btn-primary"
      ref="targetElement"
      @click="visible = !visible"
    >
      Keywords
    </button>
  
    <Wowerlay
      tag="section"
      :target="targetElement"
      v-model:visible="visible"
      style="background-color: aliceblue;"
    >
      <div v-for="keyword in props.keywordList">
        <RouterLink :to="{ name: 'movie_search_result', params: { 'category': '키워드', 'name': keyword}}" style="text-decoration: none;">
            #{{ keyword }}
        </RouterLink>
      </div>
    </Wowerlay>
  </template>
  
  <script setup lang="ts">
    import { Wowerlay } from 'wowerlay';
    import { ref, computed } from 'vue';
  
    const targetElement = ref<HTMLElement>();
    const visible = ref(false);

    const props = defineProps({
        keywordList: Object
    })
    
  </script>