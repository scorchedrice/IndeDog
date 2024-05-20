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

const helloArray = ['안녕하세요','hello','こんにちは ','bonjour ',]
</script>