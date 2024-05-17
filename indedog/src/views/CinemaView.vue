<template>
    <div class="row align-items-center container">
        <h1>CinemaView</h1>
        <h2>우선 지도를 배치하고, 해당 위치의 마크를 누르면 Detail로 연결합시다.</h2>
        <div>
            <CinemaMap/>
        </div>
        <div>
            <CinemaDetail/>
        </div>
    </div>
</template>

<script setup>
import {RouterLink, RouterView} from 'vue-router'
import CinemaMap from '@/components/CinemaMap.vue'
import CinemaDetail from '@/components/CinemaDetail.vue'
</script>

<style scoped>

</style>
