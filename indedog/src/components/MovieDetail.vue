<template>
    <h1>영화 정보</h1>
    <div class="row align-items-center">
        <img :src="curMovie.img_src" alt="movie.poster" class="col-4">
        <div class="col-8">
            <div class="row">
                <div class="col-3">
                    <vue3-star-ratings
                    v-model="score"
                    :starSize="20"
                    starColor="#ff9800"
                    inactiveColor="#333333"
                    :numberOfStars="5"
                    :disableClick="true"
                    />
                </div>
                <div class="col">
                    {{ score }} / 5.0
                </div>
            </div>
            <h2>제목 : {{ curMovie.title }}</h2>
            <p v-if="curMovie.title_en">{{ curMovie.title_en }}</p>
            <p>제작연도 : {{ curMovie.making_year }}년</p>
            <p>감독 : {{ curMovie.director }}</p>
            <p>러닝타임 : {{ curMovie.length }}</p>
            <p v-if="keywords">
                키워드 : 
                <template 
                v-for="keyword in keywords">
                    <span>
                        <RouterLink :to="{ name: 'movie_search_result', params: { 'category': '키워드', 'name': keyword}}" style="text-decoration: none;">
                            #{{ keyword }}
                        </RouterLink>
                    </span>
                </template>
            </p>
        </div>    
    </div>
    <br>
    <hr>
    <div class="row">
        <div class="col-6">
            <h1>영화 평론</h1>
            <p>해당 구역에 최근에 좋아요 많은 게시물을 표시</p>
            <hr>
            <p>해당 구역에 최근 작성 게시물 표시</p>
            <p>더보기 및 작성하기</p>
        </div>
        <div class="col-6">
            <h1>평점</h1>
            <div class="form-floating">
                <div class="row">
                    <div class="col-4">
                        <vue3-star-ratings
                            v-model="rating"
                            :starSize="20"
                            starColor="#ff9800"
                            inactiveColor="#333333"
                            :numberOfStars="5"
                            :disableClick="false"
                            />
                    </div>
                    <div class="col" >
                        {{ rating }}
                    </div>
                </div>s
                <div>
                    <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 150px"></textarea>
                    <label for="floatingTextarea2"></label>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'
import { ref, defineComponent } from 'vue'
import { useCounterStore } from '@/stores/counter.js'
import vue3StarRatings from "vue3-star-ratings"

defineComponent({
    components: {
        vue3StarRatings
    }
})


const rating = ref(0)
const score = ref(3.5)

const route = useRoute()
const curMovie = ref()

const store = useCounterStore()

for(const movie of store.movies){
    if (movie.id === Number(route.params.id)) {
        curMovie.value = movie
        break
    }
}

console.log(curMovie.value.keywords)
const keywords = curMovie.value.keywords.filter(item => item.trim() !== '')


console.log(keywords)

console.log(curMovie.value)

</script>

<style scoped>

</style>