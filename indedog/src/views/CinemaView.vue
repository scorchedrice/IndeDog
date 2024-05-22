<template>
    <div class="row align-items-center">
        <h1>현재 영화를 관람할 수 있는 상영관 및 영화 목록</h1>
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
