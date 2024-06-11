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
                <br>
                <div v-for="article in paginationArticles">
                    <RouterLink :to="{ name: 'CommunityDetailView', params: { 'id': article.id }}">
                        <h4>{{ article.title }}</h4>
                    </RouterLink>
                    <hr>
                </div>
                <div class="article-page" style="text-align: center;">
                    <vue-awesome-paginate
                    :total-items="articleList.length"
                    v-model="currentPage"
                    :items-per-page="10"
                    :max-pages-shown="5"
                    />
                </div>
            </div>
        </div>
        <br>
        
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

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import axios from 'axios'
import { Vue3Marquee } from 'vue3-marquee'

const route = useRoute()
const store = useCounterStore()
const moviesLiked = ref(null)
const articleList = ref([])
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


//pagination - 게시글
const currentPage = ref(1)
const articlesPerPage = 10
const totalPages = computed(() => Math.ceil(articleList.length / articlesPerPage))
const paginationArticles = computed(()=>{
    const start = (currentPage.value - 1)*articlesPerPage;
    const end = start + articlesPerPage;
    console.log('pageChange')
    return articleList.value.slice(start,end);
});
</script>

<style>
.article-page .pagination-container {
  column-gap: 10px;
}
.paginate-buttons {
  height: 40px;
  width: 40px;
  border-radius: 20px;
  
  cursor: pointer;
  background-color: rgb(242, 242, 242);
  border: 1px solid rgb(217, 217, 217);
  color: black;
}
.article-page .paginate-buttons:hover {
  background-color: #d8d8d8;
}
.article-page .active-page {
  background-color: #3498db;
  border: 1px solid #3498db;
  color: white;
}
.article-page .active-page:hover {
  background-color: #2988c8;
}
.article-page .back-button:active,
.article-page .next-button:active {
  background-color: #c4c4c4;
}
a {
    color: black
}
</style>