<template>
    <div>
        <form @submit.prevent="movieResult(ctName)" style="text-align: right">
            <select v-model="ctName">
                <option value="" selected>카테고리선택</option>
                <option value="감독">감독</option>
                <option value="제목">제목</option>
                <option value="키워드">키워드</option>
                <option value="제작년도">제작년도</option>
                <option value="장르">장르</option>
            </select>
            <input type="text" v-model="text">
            <input type="submit" value="검색">
        </form>

        <br>
        <div class="row align-items-center container" style="background-color: bisque; border: 5px solid black">
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
                        <h4 class="card-title">{{ movie.title }}</h4>
                        <h5 v-if="movie.title_en">{{ movie.title_en }}</h5>
                        <h6 class="card-text">{{ movie.making_year }}</h6>
                    
                        <h6 class="list-group-item">Director: {{ movie.director }}</h6>
                        <h6 class="list-group-item">Genre: {{ movie.genre }}</h6>
                        <h6 class="list-group-item">Running Time: {{ movie.length }}</h6>
                        <Keyword :keyword-list="movie.keywords" />
                    </div>
                    
                </div>
                <br>
                <hr>
            </div>
            </div>
        </div>
        <fwb-pagination style="text-align: center" v-model="currentPage" :total-pages="totalPages" previous-label="⬅️" next-label="➡️"></fwb-pagination>
        <br>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { FwbPagination } from 'flowbite-vue'
import { ref, computed } from 'vue'
import Keyword from '@/components/KeywordDetail.vue'

const text = ref('')
const ctName = ref('')
const router = useRouter()

const store = useCounterStore()
const movies = store.movies
const searchedMovies = ref([])

const movieResult = function (category) {
    router.push({ name: 'movie_search_result', params: { 'category': category, 'name': text.value }})
}


// pagination
const currentPage = ref(1)
const moviesPerPage = 6
const totalPages = computed(() => Math.ceil(movies.length / moviesPerPage))
const paginationMovies = computed(()=>{
    const start = (currentPage.value - 1)*moviesPerPage;
    const end = start + moviesPerPage;
    console.log('pageChange')
    return movies.slice(start,end);
});

</script>

<style scoped>
@import '@/assets/font/font.css';
h4,h3 {
    font-family: "hanna";
}
* {
    font-family: "hanna_air"
}
</style>