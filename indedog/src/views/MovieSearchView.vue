<template>
    <div>
        <h1>작품을 검색하는 View입니다.</h1>
        <h2>크롤링을 통해 구축한 DB를 활용해 렌더링합니다.</h2>
        <div 
        v-for="movie in movies"
        :key="movie.id">
            <img :src="movie.img_src" alt="movie.poster" width="500px">
            {{ movie.title }}
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'
const store = useCounterStore()

const movies = store.movies

</script>

<style scoped>

</style>