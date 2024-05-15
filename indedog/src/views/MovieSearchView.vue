<template>
    <div>
        <h1>작품을 검색하는 View입니다.</h1>
        <h2>크롤링을 통해 구축한 DB를 활용해 렌더링합니다.</h2>
        <h3>{{ movies.length }}</h3>
        <h3>{{ totalPages }}</h3>
        <div 
        v-for="movie in paginationMovies"
        :key="movie.id">
            <img :src="movie.img_src" alt="movie.poster" width="500px">
            {{ movie.title }}
            {{ movie.id }}
            <hr>
        </div>
        <fwb-pagination v-model="currentPage" :total-pages="totalPages" previous-label="⬅️" next-label="➡️"></fwb-pagination>
        <br>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { FwbPagination } from 'flowbite-vue'
import { ref, computed } from 'vue'

const store = useCounterStore()
const movies = store.movies

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