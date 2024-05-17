<template>
    <div>
        <h1>상영관의 정보를 담고 있습니다.</h1>
        <p>해당 상영관의 길찾기, 상영중인 영화 등의 정보를 제공합니다.</p>
        <div v-for="movie in recentMovie" class="row align-items-center">
            <img :src="movie.img_src" alt="movie_poster" class="col-4">
            <div class="col-8">
                <h3>{{ movie.title }} - {{ movie.director }}</h3>
                <p>장르: {{ movie.genre }}</p>
                <p>상영시간: {{ movie.length }}</p>
                <div 
                v-for="cinema in movie.cinemas"
                >
                    <div v-if="cinema != ''">
                        <RouterLink :to="{name:'cinema_info', params: {'address': cinema}}">
                            {{ cinema }}
                        </RouterLink>
                    </div>
                </div>
            </div>
            <p></p>
            <hr>
        </div>
        
    </div>
</template>

<script setup>

import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

const store = useCounterStore()
const movieList = store.movies
const recentMovie = ref([])
const cinemaList = ref([])
// 키워드를 중심으로 검색
// 현재 상영중인 영화는 id 10000번대부터 설정, id 1만번대부터 검색
for (const movie of movieList) {
    if (Number(movie.id) >= 10000) {
        recentMovie.value.push(movie)
    }
}


</script>

<style scoped>

</style>
