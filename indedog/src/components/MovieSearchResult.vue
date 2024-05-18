<template>
    <div>
        <h1>검색 결과 "{{route.params.category}} : {{ route.params.name }}"</h1>
        <ul v-for="movie in paginationMovies">
            <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                    <img :src="movie.img_src" alt="movie.poster" width="500px">
            </RouterLink>
            {{ movie.title }}
        </ul>
        <fwb-pagination style="text-align: center" v-model="currentPage" :total-pages="totalPages" previous-label="⬅️" next-label="➡️"></fwb-pagination>
    </div>
</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
import { FwbPagination } from 'flowbite-vue'
import { ref, computed } from 'vue'

const store = useCounterStore()
const route = useRoute()
const currentMovies = ref([])
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
        if (movie.keywords.split('#').includes(route.params.name)){
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