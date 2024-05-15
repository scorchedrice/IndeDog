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
        <naver-marker
        latitude="37.51347"
        longitude="127.041722"
        />
    </naver-map>
</template>

<script setup>
import { NaverMap, NaverMarker } from 'vue3-naver-maps'

const mapOptions = {
  latitude: 37.51347, // 지도 중앙 위도
  longitude: 127.041722, // 지도 중앙 경도
  zoom: 13,
  zoomControl: true,
  }
</script>

<style scoped>

</style>
