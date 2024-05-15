<template>
    <div class = "container row align-items-center">
        <div class="col-8">
            <h1>오늘의 추천 영화</h1>
            <h4>
                오늘은 석가탄신일! 불교와 관련된 독립영화 어때요?
            </h4>
            <p class="keyword">#불교</p>
        </div>
        <div class="col-4">
            <div id="carousel_today_recommend" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner">
                    <template v-for="(tdmovie, index) in todayMovie"
                    :key="tdmovie.id">
                    <div class="carousel-item active"
                    v-if="index == 0">
                        <img :src="tdmovie.img_src" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item"
                    v-if="index > 0">
                        <img :src="tdmovie.img_src" class="d-block w-100" alt="...">
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
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const store = useCounterStore()
const movieList = store.movies
console.log(movieList)
const todayMovie = ref([])

// 키워드를 중심으로 검색
// 현재 상영중인 영화는 id 10000번대부터 설정, id 1만번대부터 검색
for (const movie of movieList) {
    if (movie.keywords.includes('#불교')){
        console.log(movie)
        todayMovie.value.push(movie)
    }
}


</script>

<style scoped>

</style>