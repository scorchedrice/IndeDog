<template>
    <div>
        <h1>영화 정보</h1>
        <img :src="curMovie.img_src" alt="movie.poster">
        <hr>
        <h2>제목 : {{ curMovie.title }}</h2>
        <p>감독 : {{ curMovie.director }}</p>
        <p>키워드 : {{ curMovie.keywords }}</p>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const route = useRoute()
const curMovie = ref()
const store = useCounterStore()

for(const movie of store.movies){
    if (movie.id === Number(route.params.id)) {
        curMovie.value = movie
        break
    }
}

console.log(curMovie.value)

</script>

<style scoped>

</style>