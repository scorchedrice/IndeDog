<template>
    <Vue3Marquee>
        <span
            v-for="(word, index) in helloArray"
            :key="index"
        >
            {{ word }}
        </span>
    </Vue3Marquee>
</template>

<script setup>
import { Vue3Marquee } from 'vue3-marquee'

const helloArray = ['좌상단 강아지바 클릭!']
</script>