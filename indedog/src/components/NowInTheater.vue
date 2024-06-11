<template>
    <header>
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
// 현재 상영중인 영화의 id 정보
const recentMovieIdList = ref([5242, 5246, 5293, 5311])
for (movie in movieList.value) {
    console.log('###')
    console.log(movie.id)
    console.log('###')
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
