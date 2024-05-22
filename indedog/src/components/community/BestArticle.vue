<template>
    <div>
        <br>
        <article v-for="article in articleList"
        :key="article.id">
                <h3>[{{ article.category }}] {{ article.title }}</h3>
                <p>{{ article.content }}</p>
                <!-- <RouterLink :to="{ name: 'CommunityDetailView', params: { id: article.id }}">
                    <h3>{{ article.title }}</h3>
                </RouterLink> -->
                <hr>
        </article>
    </div>
</template> 

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

const category = ref('전체')
const store = useCounterStore()
console.log(store.articles)
let articleList = store.articles.sort((a,b) => {
    if (a.like_users > b.like_users) return -1;
    if (a.like_users < b.like_users) return 1;
    return 0;
});
console.log(articleList)




</script>

<style scoped>
</style>