<template>
    <div>
        <h1>CinemaView</h1>
        <h2>이곳에 상영관 정보를 나열합니다.</h2>
        <button>
            <RouterLink :to="{name: 'cinema_detail'}">
                detail example
            </RouterLink>
        </button>
        <RouterView/>
    </div>
</template>

<script setup>
import {RouterLink, RouterView} from 'vue-router'
</script>

<style scoped>

</style>
