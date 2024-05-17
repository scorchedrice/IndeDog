<template>
    <div>
        <h1>상영관의 정보를 담고 있습니다.</h1>
        <p>해당 상영관의 길찾기, 상영중인 영화 등의 정보를 제공합니다.</p>
    </div>
</template>

<script setup>

import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'
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

</style>
