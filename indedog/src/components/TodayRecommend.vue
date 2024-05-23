<template>
    <div class = "align-items-center" style="text-align: center;">
        <h2>운영자의 선택 !</h2>
        <div style="text-align: center;">
            <div class="row">
                <div id="carousel_today_recommend" class="carousel slide col-6" data-bs-ride="carousel" style="margin: auto;">
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
                5월 22일은 국제 생물 다양성의 날! 자연을 다루는 영화는 어때요?
            </h4>
            <p class="keyword">#자연, #생명</p>
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
    if (movie.keywords.includes('자연') || movie.keywords.includes('생명')){
        todayMovie.value.push(movie)
    }
}


</script>

<style scoped>
@import '@/assets/font/font.css';
h1,h2 {
    font-family: "hanna";
}
* {
    font-family: "hanna_air"
}

#carousel_today_recommend{
    width: 50%;
}
</style>