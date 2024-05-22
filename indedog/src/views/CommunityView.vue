<template>
    <div style="border: solid black 5px;">
        <BestArticle/>
    </div>
    <br>
    <div style="border: solid black 5px;">
        
            <MovieCommunity/>
        
    </div>
    <br>
    <div style="border: solid black 5px">
            <TheaterCommunity/>
    </div>
    <br>
    <div>
        <RouterLink :to="{ name: 'CommunityCreateView'}">
            <h1>게시글 작성</h1>
        </RouterLink>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BestArticle from '@/components/community/BestArticle.vue'
import MovieCommunity from '@/components/community/MovieCommunity.vue'
import MovieComment from '@/components/community/MovieComment.vue'
import TheaterCommunity from '@/components/community/TheaterCommunity.vue'
const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>