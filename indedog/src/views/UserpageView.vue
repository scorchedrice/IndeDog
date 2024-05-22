<template>
    <div>
        <h1>{{ userName }}</h1>님의 유저페이지 입니다.
        <hr>
        <div class="row">
            <div class="col-6" style="height: 500px;">
                <h2>좋아요한 작품</h2>
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#staticBackdrop" style="border: solid black;">
                    {{ userName }}님이 좋아하는 영화들 펼쳐보기
                </button>
                <div style="width: 95%;">
                    <Vue3Marquee
                        :clone="true"
                        :duration="50"
                        :direction="'reverse'"
                        :pause-on-hover="true"
                        @on-pause="playState = 'paused'"
                        @on-resume="playState = 'playing'"
                        aria-setsize="small"
                    >
                        <span v-for="movie in moviesLiked" style="text-align: center;">
                            <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id }}">
                                <img :src="movie.img_src" alt="poster" style="height: 50vh;">
                            </RouterLink>
                            <h5>{{ movie.title }}</h5>
                        </span>
                    </Vue3Marquee>
                </div>
            </div>
            <div class="col-6">
                <h2>작성한 게시글</h2>
                <div v-for="article in articleList">
                    <RouterLink :to="{ name: 'CommunityDetailView', params: { 'id': article.id }}">
                        <h2>{{ article.title }}</h2>
                    </RouterLink>
                </div>
            </div>
        </div>
        <br>
        <hr>
    </div>


    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-scrollable modal-xl">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ userName }}님이 좋아하는 작품들</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <div v-for="movie in moviesLiked" class="row align-items-center">
                <div class="col-4">
                    <img :src="movie.img_src" alt="" style="height: 300px;">
                </div>
                <div class="col-8">
                    <h1>{{ movie.title }}</h1>
                    <h4>{{ movie.genre }}</h4>
                    <h6>{{ movie.keywords }}</h6>
                </div>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Understood</button>
        </div>
        </div>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import axios from 'axios'
import { Vue3Marquee } from 'vue3-marquee'

const route = useRoute()
const store = useCounterStore()
const moviesLiked = ref(null)
const articleList = ref(null)
const userName = ref(route.params.username)

console.log(route.params.username)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/custom/user/${userName.value}/`,
    })
        .then(res => {
        console.log(res)
        moviesLiked.value = res.data.like_movies
        articleList.value = res.data.article_set
    })
        .catch(err => {
            console.log(err)
        })
})


</script>

<style scoped>

</style>