<template>
    <div class="row align-items-center">
        <div class="list-group col">
            <button type="button" class="list-group-item list-group-item-action active" aria-current="true">
                로그인
            </button>
            <button type="button" class="list-group-item list-group-item-action">작품 검색</button>
            <button type="button" class="list-group-item list-group-item-action"
            @click="moveToCinemaView">상영관 검색</button>
            <button type="button" class="list-group-item list-group-item-action">현재 상영작</button>
            <button type="button" class="list-group-item list-group-item-action">커뮤니티</button>
        </div>
    </div>
</template>

<script setup>
import {useRoute, useRouter} from 'vue-router';
const router = useRouter()
const moveToCinemaView = function () {
    console.log('moveToCinemaView')
    router.push({name:'cinema_list'})
}
</script>

<style scoped>

</style>
