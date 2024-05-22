<template>
    <div>
        <h1>검색 결과</h1>
        <h3>
        "{{route.params.category}} 항목에서 {{ route.params.name }}을(를) 검색한 결과입니다."</h3>
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
                        <h5 class="card-title">{{ movie.title }}</h5>
                        <h6 v-if="movie.title_en">{{ movie.title_en }}</h6>
                        <p class="card-text">{{ movie.making_year }}</p>
        
                        <li class="list-group-item">Director: {{ movie.director }}</li>
                        <li class="list-group-item">Genre: {{ movie.genre }}</li>
                        <li class="list-group-item">Running Time: {{ movie.length }}</li>
                        <Keyword :keyword-list="movie.keywordws" />
                    </div>
                    
                </div>
                <br>
                <hr>
            </div>
            </div>
        <fwb-pagination style="text-align: center;" v-model="currentPage" :total-pages="totalPages" previous-label="⬅️" next-label="➡️"></fwb-pagination>
    </div>
</template>

<script setup>
import { useRoute, useRouter, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import { FwbPagination } from 'flowbite-vue'
import { ref, computed } from 'vue'
import Keyword from '@/components/KeywordDetail.vue'
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

console.log(currentMovies.value)


const text = ref('')
const currentPage = ref(1)
const moviesPerPage = 6
const totalPages = computed(() => Math.ceil(currentMovies.value.length / moviesPerPage))
const paginationMovies = computed(()=>{
    const start = (currentPage.value - 1)*moviesPerPage;
    const end = start + moviesPerPage;
    return currentMovies.value.slice(start,end);
});
</script>

<style scoped>

</style>