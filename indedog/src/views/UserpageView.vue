<template>
    <div>
        <h1>{{ userName }}</h1>님의 유저페이지 입니다.
        <hr>
        <div>
            <h2>좋아요한 작품</h2>
            <span v-for="movie in moviesLiked">
                <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id }}">
                    <img :src="movie.img_src" alt="poster">
                </RouterLink>
            </span>
        </div>
        <hr>
        <h2>작성한 게시글</h2>
        <div v-for="article in articleList">
            <RouterLink :to="{ name: 'CommunityDetailView', params: { 'id': article.id }}">
                <h2>{{ article.title }}</h2>
            </RouterLink>
        </div>
        
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import axios from 'axios'

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