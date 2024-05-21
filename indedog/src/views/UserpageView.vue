<template>
    <div>
        <h1>{{ store.loginUser }}</h1>님의 유저페이지 입니다.
        <hr>
        <div>
            <h2>좋아요한 작품</h2>
        </div>
        <hr>
        <div>
            <h2>작성한 게시글</h2>
        </div>
        
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter.js'

const store = useCounterStore()

</script>

<style scoped>

</style>