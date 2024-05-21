<template>
    <div>
        <div v-for="movie in recentMovie" class="row align-items-center">
            <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }" class="col-4">
                    <img :src="movie.img_src" class="d-block w-100" alt="...">
            </RouterLink>
            <div class="col-8">
                <h3>{{ movie.title }} - {{ movie.director }}</h3>
                <p>장르: {{ movie.genre }}</p>
                <p>상영시간: {{ movie.length }}</p>
                <div 
                v-for="cinema in cinemaList[movie.id]"
                >
                    <div v-if="cinema != ''">
                        <RouterLink :to="{name:'cinema_info', params: {'address': cinema}}">
                            {{ cinema }}
                        </RouterLink>
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
const isFirstMount = ref(true)
const store = useCounterStore()
const recentMovie = store.recentMovies
const cinemaList = ref({})
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

</style>
