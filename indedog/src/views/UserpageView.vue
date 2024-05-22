<template>
    <div>
        <h1>{{ store.loginUser }}</h1>님의 유저페이지 입니다.
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
        <div>
            <h2>작성한 게시글</h2>
        </div>
        
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import axios from 'axios'

const store = useCounterStore()
const moviesLiked = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/admin/user/${store.loginPk}/`,
    })
      .then(res => {
        console.log(res)
        moviesLiked.value = res.data.like_movies
      })
})


</script>

<style scoped>

</style>