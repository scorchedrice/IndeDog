<template>
    <div>
        <h1>작품을 검색하는 View입니다.</h1>
        <h2>크롤링을 통해 구축한 DB를 활용해 렌더링합니다.</h2>
        <br>
        <h3>디버깅용 {{ movies.length }}</h3>
        <h3>{{ totalPages }}</h3>
        <form @submit.prevent="movieResult(ctName)" style="text-align: center">
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
        <ul
        v-for="movie in paginationMovies"
        :key="movie.id">
            <li>
                <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                    <img :src="movie.img_src" alt="movie.poster" width="500px">
                </RouterLink>
                {{ movie.title }}
                {{ movie.id }}
            </li>
            <hr>
        </ul>
        <fwb-pagination style="text-align: center" v-model="currentPage" :total-pages="totalPages" previous-label="⬅️" next-label="➡️"></fwb-pagination>
        <br>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { FwbPagination } from 'flowbite-vue'
import { ref, computed } from 'vue'

const text = ref('')
const ctName = ref('')
const router = useRouter()

const store = useCounterStore()
const movies = store.movies
const searchedMovies = ref([])

const movieResult = function (category) {
    console.log(category)
    router.push({ name: 'movie_search_result', params: { 'category': category, 'name': text.value }})
}


// pagination
const currentPage = ref(1)
const moviesPerPage = 6
const totalPages = computed(() => Math.ceil(movies.length / moviesPerPage))
const paginationMovies = computed(()=>{
    const start = (currentPage.value - 1)*moviesPerPage;
    const end = start + moviesPerPage;
    return movies.slice(start,end);
});

</script>

<style scoped>

</style>