<template>
    <div class = "align-items-center" style="text-align: center;">
        <div style="text-align: center;">
            <h1>오늘의 추천 영화!</h1>
            <div>
                <div id="carousel_today_recommend" class="carousel slide" data-bs-ride="carousel" style="margin: auto;">
                    <div class="carousel-inner">
                        <template v-for="(tdmovie, index) in todayMovie"
                        :key="tdmovie.id">
                        <div class="carousel-item active"
                        v-if="index == 0">
                        <RouterLink :to="{ name: 'movie_detail', params: { 'id': tdmovie.id } }">
                            <img :src="tdmovie.img_src" class="d-block w-100" alt="...">
                        </RouterLink>
                    </div>
                    <div class="carousel-item"
                    v-if="index > 0">
                    <RouterLink :to="{ name: 'movie_detail', params: { 'id': tdmovie.id } }">
                        <img :src="tdmovie.img_src" class="d-block w-100" alt="...">
                    </RouterLink>
                </div>
            </template>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carousel_today_recommend" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carousel_today_recommend" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</div>
</div>
<div>
            <h4>
                오늘은 석가탄신일! 불교와 관련된 독립영화 어때요?
            </h4>
            <p class="keyword">#불교</p>
        </div>   
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import AIRecommend from '@/components/AIRecommend.vue'

const store = useCounterStore()
const movieList = store.movies
const todayMovie = ref([])

for (const movie of movieList) {
    if (movie.keywords.includes('불교')){
        todayMovie.value.push(movie)
    }
}


</script>

<style scoped>
@import '@/assets/font/font.css';
h1 {
    font-family: "hanna";
}
* {
    font-family: "hanna_air"
}

#carousel_today_recommend{
    width: 50%;
}
</style>