<template>
    <div style="width: auto;">
        <Vue3Marquee
            :pause-on-hover="true"
            @on-pause="playState = 'paused'"
            @on-resume="playState = 'playing'"
            aria-setsize="small"
        >
            <div v-for="movie in recentMovies" :key="movie.id">
                <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                    <img :src="movie.img_src" class="d-block w-100" alt="...">
                </RouterLink>
                <h2>{{ movie.title }}</h2>
                <!-- <h3>{{ movie.title_en }}</h3> -->
                <h4>{{ movie.genre }}</h4>
            </div>
        </Vue3Marquee>
    </div>
    <p>
        마우스를 올리시면 애니메이션이 멈춥니다.
    </p>
</template>

<script setup>
import { ref } from 'vue'
import { Vue3Marquee } from 'vue3-marquee'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

// 1. Data
const store = useCounterStore()
const recentMovies = store.recentMovies
// 현재 상영중인 영화의 id 정보

const playState = ref('playing')
</script>