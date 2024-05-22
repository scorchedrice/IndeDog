<template>
    <div class="row align-items-center">
        <div class="col-6" v-for="movie in recentMovie">
            <div class="row align-items-center">
                <div class="col-6">
                    <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }" class="col-4">
                            <img :src="movie.img_src" class="d-block w-100" alt="...">
                    </RouterLink>
                </div>
            
            <div class="col-6">
                <h4>{{ movie.title }}</h4>
                <h5 v-if="movie.title_en">{{ movie.title_en }}</h5>
                <h6>{{ movie.making_year }}</h6>

                <h6>Director: {{ movie.director }}</h6>
                <h6>Genre: {{ movie.genre }}</h6>
                <h6>Running Time: {{ movie.length }}</h6>
                <div>
                    <!-- ------------- -->
                    <hr>
                    <div class="btn-group dropend">
                        <button type="button" class="btn dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            상영관
                        </button>
                        <ul class="dropdown-menu" style="width: 30vh">
                            <div 
                        v-for="cinema in cinemaList[movie.id]"
                        >
                            <div v-if="cinema != ''">
                                <h6 @click="goCinemaInfo(cinema)">{{ cinema }}</h6>
                            </div>
                        </div>
                        </ul>
                    </div>
                    <!-- ------------- -->
                        
                </div>
            </div>
        </div>
            <p></p>
            <hr>
        </div>
        
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import router from '@/router';
const gorouter = useRouter()
const isFirstMount = ref(true)
const store = useCounterStore()
const recentMovie = store.recentMovies
const cinemaList = ref({})
const goCinemaInfo = function (cinema) {
    gorouter.push({name:'cinema_info', params: {'address': cinema}})
}

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/cinemas/`
    })
      .then( res => {
        console.log(res.data)
        for (const cinema in res.data) {
            for (const targetMovie in res.data[cinema].recent_movies) {
                let temp = res.data[cinema].recent_movies[targetMovie]
                if (cinemaList.value[temp] == undefined) {
                cinemaList.value[temp] = [res.data[cinema].address]
                } else if (cinemaList.value[temp] != undefined) {
                    cinemaList.value[temp].push(res.data[cinema].address)
                }
            }
        }
        console.log(cinemaList.value)
      })
})
</script>

<style scoped>
@import '@/assets/font/font.css';
h4 {
    font-family: 'hanna'
}
</style>
