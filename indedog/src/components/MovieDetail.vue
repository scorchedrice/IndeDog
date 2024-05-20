<template>
    <div>
        <h1>영화 정보</h1>
        <img :src="curMovie.img_src" alt="movie.poster">
        <hr>
        <h2>제목 : {{ curMovie.title }}</h2>
        <p v-if="curMovie.title_en">{{ curMovie.title_en }}</p>
        <p>감독 : {{ curMovie.director }}</p>
        
        <p v-if="keywords">
            키워드 : 
            <template 
            v-for="keyword in keywords">
            <span>
                <RouterLink :to="{ name: 'movie_search_result', params: { 'category': '키워드', 'name': keyword}}" style="text-decoration: none;">
                    #{{ keyword }}
                </RouterLink>
                </span>
            </template>
        </p>
    </div>
</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'
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

console.log(curMovie.value.keywords)
const keywords = curMovie.value.keywords.filter(item => item.trim() !== '')


console.log(keywords)

console.log(curMovie.value)

</script>

<style scoped>

</style>