<template>
    <h1>공지사항</h1>
    <div v-if="store.isStaff">
        <RouterLink :to="{ name: 'CommunityCreateView'}">
            <h5>공지사항 작성</h5>
        </RouterLink>
    </div>
    <hr>
    <article v-for="article in articles" :key="article.id">
        <RouterLink :to="{ name: 'CommunityDetailView', params: { 'id': article.id}}">
            <h3>{{ article.title }}</h3>
        </RouterLink>
        <br>
    </article>
</template>

<script setup>
import {useCounterStore} from '@/stores/counter.js'
import {ref, onMounted} from 'vue'
import {RouterLink} from 'vue-router'

const articles = ref([])
const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

for (const article of store.articles){
    console.log(article)
    console.log('##')
    if (article.is_notice) {
        articles.value.push(article)
    }
}


</script>

<style scoped>

</style>