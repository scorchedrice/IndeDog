<template>
    <div class = "row">
        <div class="col-6" style="border: 5px solid black">
            <h1>Notice</h1>
            <h1>가장 최근 공지</h1>
            <hr>
            <RouterLink v-if="articlesLatest" :to="{ name: 'CommunityDetailView', params: { 'id': articlesLatest.id}}">
                <h1>{{ articlesLatest.title }}</h1>
            </RouterLink>

        </div>
        <div class="col-1"></div>
        <div class="col-5" style="border: 5px solid black">
            <h2>최근 공지 목록</h2>
            <hr>
            <div v-for="article in articles" style="position: flex; ">
                <div>
                    <RouterLink :to="{ name: 'CommunityDetailView', params: { 'id': article.id }}">
                        {{ article.title }} 
                    </RouterLink>
                </div>
                <div>
                    {{ article.updated_at }}
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import {useCounterStore} from '@/stores/counter.js'
import {ref, onMounted} from 'vue'
import {RouterLink} from 'vue-router'

const articles = ref([])
const store = useCounterStore()
const articlesLatest = ref(null)

onMounted(() => {
  store.getArticles()
})

for (const article of store.articles){
    if(article.is_notice){
        articles.value.push(article)
    }
}

if(articles.value.length){
    articlesLatest.value = articles.value[articles.value.length-1]
}
console.log(articlesLatest.value)

</script>

<style scoped>
h1,h2 {
    font-family: "hanna";
}
* {
    font-family: "hanna_air"
}
</style>
