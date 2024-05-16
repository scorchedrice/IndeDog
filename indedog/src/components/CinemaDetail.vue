<template>
    <div>
        <h1>영화관의 세부 정보를 이곳에 나타냅니다.</h1>
        <p>지도, 주소, 상영관에서 현재 상영하고 있는 영화를 나타냅니다.</p>
        <p>나중에 데이터가 오면 cinemaId를 받고 이에 적합한 화면을 렌더링 합니다.</p>
        <p>index.js 등 많은 값의 수정이 필요합니다.</p>
        
    </div>
    <naver-map
    style="width: 100%; height: 400px"
    :map-options="mapOptions"
    >
        <naver-marker id="markerexample"
            latitude = "37.51347"
            longitude = "127.041722"     
            @click="onMarkerClicked"
        >
           <img src="@/assets/icon/marker_icon.jpg" alt="marker" 
           style="border-radius: 80%;"
           >
        </naver-marker>
        <naver-info-window
        marker="#markerexample"
        :open="true"
        >
            
        </naver-info-window>
    </naver-map>
    <CinemaMap/>
</template>

<script setup>
import { NaverMap, NaverMarker, NaverInfoWindow } from 'vue3-naver-maps'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'
import CinemaMap from "@/components/CinemaMap.vue"


const store = useCounterStore()
const movieList = store.movies
const recentMovie = ref([])

// 키워드를 중심으로 검색
// 현재 상영중인 영화는 id 10000번대부터 설정, id 1만번대부터 검색
for (const movie of movieList) {
    if (Number(movie.id) >= 10000) {
        recentMovie.value.push(movie)
    }
}

const recentMovieFirst = recentMovie.value[0]

const mapOptions = {
  latitude: 37.51347, // 지도 중앙 위도
  longitude: 127.041722, // 지도 중앙 경도
  zoom: 13,
  zoomControl: true,
  }
// marker-event
const onMarkerClicked = function (event) {
    console.log(event.currentTarget)
    console.log(event.target)
    console.log(event.coord)
}

</script>

<style scoped>

</style>
