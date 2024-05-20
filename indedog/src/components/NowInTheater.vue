<template>
    <header style="border: 5px solid black;">
        <div>
            <h1>현재 상영중</h1>
            <MarqueeNowInTheater/>
        </div>
    </header>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import Notice from '@/components/Notice.vue'
import MarqueeNowInTheater from '@/components/slide/MarqueeNowInTheater.vue'

const store = useCounterStore()
const movieList = store.movies
const recentMovie = ref([])

// 키워드를 중심으로 검색
// 현재 상영중인 영화는 id 10000번대부터 설정, id 1만번대부터 검색
for (const movie of movieList) {
    if (Number(movie.id) >= 10000) {
        recentMovie.value.push(movie)
    }
}

const recentMovieFirst = recentMovie.value[0]

</script>

<style scoped>
@import '@/assets/font/font.css';
h1,h2 {
    font-family: "hanna";
    text-align: center;
}
* {
    font-family: "hanna_air"
}
</style>
