<template>
    <div v-if="store.isStaff">
        당신은 스태프입니다.
        <RouterLink :to="{ name: 'CommunityCreateView'}">
            <button>
                공지사항 작성
            </button>
        </RouterLink>
    </div>
    <h3>제목 |</h3>
    <hr>
    <article v-for="article in articles" :key="article.id">
        <RouterLink :to="{ name: 'CommunityDetailView', params: { 'id': article.id}}">
            <h3>공지 | {{ article.title }}</h3>
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
    if(article.is_notice){
        articles.value.push(article)
    }
}


</script>

<style scoped>

</style>