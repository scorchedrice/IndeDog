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
import { RouterLink, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'


const isFirstMount = ref(true)
const store = useCounterStore()
const recentMovie = store.recentMovies
const cinemaList = ref([])


</script>

<style scoped>

</style>
