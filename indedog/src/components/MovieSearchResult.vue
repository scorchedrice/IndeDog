<template>
    <div>
        <h1>검색 결과</h1>
        <h3>
        "{{route.params.category}} 항목에서 {{ route.params.name }}을(를) 검색한 결과입니다."</h3>
        <div display="flex">
            <form @submit.prevent="movieResult(ctName)" style="display: flex; width: 500px; margin-left: auto">
                <div class="input-group input-group-sm mb-3">
                    <select class="form-select" v-model="ctName" style="width: 140px;">
                        <option value="" selected>카테고리 선택</option>
                        <option value="감독">감독</option>
                        <option value="제목">제목</option>
                        <option value="키워드">키워드</option>
                        <option value="제작년도">제작년도</option>
                        <option value="장르">장르</option>
                    </select>
                    <input type="text"  class="form-control" v-model="text" style="width: 300px">
                </div>
                <input type="submit" value="검색" style="width: 60px; height: 100%;">
            </form>
        </div>
        <div class="row align-items-center">
            <div
            v-for="movie in paginationMovies"
            :key="movie.id" class="col-6">
                <br>
                <div class="container row">
                    <div class="col-6">
                        <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                            <img :src="movie.img_src" alt="movie.poster" width="100%">
                        </RouterLink>
                    </div>

                    <div class="col-6">
                        <h5 class="card-title">{{ movie.title }}</h5>
                        <h6 v-if="movie.title_en">{{ movie.title_en }}</h6>
                        <p class="card-text">{{ movie.making_year }}</p>
        
                        <li class="list-group-item">Director: {{ movie.director }}</li>
                        <li class="list-group-item">Genre: {{ movie.genre }}</li>
                        <li class="list-group-item">Running Time: {{ movie.length }}</li>
                        <hr>
                        <div class="btn-group dropend">
                        <button type="button" class="btn dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            Keywords
                        </button>
                        <ul class="dropdown-menu" style="width: 20vh">
                            <div 
                        v-for="keyword in movie.keywords"
                        >
                            <div v-if="keyword != ''">
                                <h6 @click="goMovieDetail(keyword)">#{{ keyword }}</h6>
                            </div>
                        </div>
                        </ul>
                        </div>
                    </div>
                </div>
                <br>
                <hr>
            </div>
            </div>
        </div>
        <br>
        <div style="text-align: center;">
        <div class="movie-page">
            <vue-awesome-paginate
            :total-items="currentMovies.length"
            v-model="currentPage"
            :items-per-page="6"
            :max-pages-shown="5"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import { useRoute, useRouter, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import { ref, computed } from 'vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const currentMovies = ref([])
const ctName = ref(route.params.category)

const movieResult = function (category) {
    router.push({ name: 'movie_search_result', params: { 'category': category, 'name': text.value }})
    .then(() => {
    window.location.reload()});
}
const goMovieDetail = function (keyword) {
    router.push({name: 'movie_search_result', params:{'category': '키워드', 'name':keyword}})
    .then(() => {
    window.location.reload()});
}
console.log(route.params)
if (route.params.category === '제목'){
    for (const movie of store.movies){   
        if (movie.title.includes(route.params.name) || movie.title_en.includes(route.params.name)){
            currentMovies.value.push(movie)
        }
    }
}
else if (route.params.category === '감독'){
    for (const movie of store.movies){   
        if (movie.director.includes(route.params.name)){
            currentMovies.value.push(movie)
        }
    }
}
else if (route.params.category === '키워드'){
    for (const movie of store.movies){  
        if (movie.keywords.includes(route.params.name)){
            currentMovies.value.push(movie)
        }
    }
}
else if (route.params.category === '제작년도'){
    for (const movie of store.movies){   
        if (movie.making_year.includes(route.params.name)){
            currentMovies.value.push(movie)
        }
    }
}
else if (route.params.category === '장르'){
    for (const movie of store.movies){   
        if (movie.genre.includes(route.params.name)){
            currentMovies.value.push(movie)
        }
    }
}

console.log('CURRENTMOVIE')
console.log(currentMovies.value)

const text = ref('')

// pagination
const currentPage = ref(1)
const moviesPerPage = 6
const totalPages = computed(() => Math.ceil(currentMovies.value.length / moviesPerPage))
const paginationMovies = computed(()=>{
    const start = (currentPage.value - 1)*moviesPerPage;
    const end = start + moviesPerPage;
    return currentMovies.value.slice(start,end);
});
</script>

<style>

.movie-page .pagination-container {
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
.movie-page .paginate-buttons:hover {
  background-color: #d8d8d8;
}
.movie-page .active-page {
  background-color: #3498db;
  border: 1px solid #3498db;
  color: white;
}
.movie-page .active-page:hover {
  background-color: #2988c8;
}
.movie-page .back-button:active,
.movie-page .next-button:active {
  background-color: #c4c4c4;
}

</style>