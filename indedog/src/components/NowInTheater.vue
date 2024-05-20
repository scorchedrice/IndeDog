<template>
    <div class = "container">
        <h1>상영중인 영화</h1>
        <div id="carousel_now_in_theater" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
            <div v-for="movie in recentMovie"
                :key="movie.id">
                <div v-if="movie.id==10000" class="carousel-item active">
                    <div class="container row align-items-center">
                        <div class="col-4">
                            <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                               <img :src="movie.img_src" class="d-block w-100" alt="...">
                            </RouterLink>
                        </div>
                        <div class="col-8">
                            <h2>{{ movie.title }} - {{ movie.director }}</h2>
                            <p>장르: {{ movie.genre }}</p>
                            <p>{{ movie.keyword }}</p>
                        </div>
                    </div>
                </div>
                <div v-if="movie.id>10000" class="carousel-item">
                    <div class="container row align-items-center">
                        <div class="col-4">
                            <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                                <img :src="movie.img_src" class="d-block w-100" alt="...">
                            </RouterLink>
                        </div>
                        <div class="col-8">
                            <h2>{{ movie.title }}</h2>
                            <p>{{ movie.genre }}</p>
                            <p>{{ movie.cinemas }}</p>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carousel_now_in_theater" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carousel_now_in_theater" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
            </button>
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
