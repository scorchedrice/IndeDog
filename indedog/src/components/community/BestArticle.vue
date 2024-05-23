<template>
    <div>
        <br>
        <h2 style="text-align: center;">오늘의 "Hot"한 게시물</h2>
        <br>
        <article v-for="article in articleList"
        :key="article.id">
                <div v-if="article.category!='공지'">
                    <h4>[{{ article.category }}] {{ article.title }}</h4>
                    <div v-if="article.content.length > 25">
                        <p>{{ article.content.slice(0,25) }}...  - 좋아요: {{ article.like_users.length }}개</p>
                    </div>
                    <div v-else>
                        <p>{{ article.content }} - 좋아요: {{ article.like_users.length }}개</p>
                    </div>
                </div>
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
    if (a.like_users.length > b.like_users.length) return -1;
    if (a.like_users.length < b.like_users.length) return 1;
    return 0;
});

console.log(articleList)
const cuttingIndex = ref(0)
for (const article of articleList) {
    console.log(article)
    console.log('####')
    if (article.category != '공지') {
        cuttingIndex.value++
    }
    if (cuttingIndex.value == 4) {
        articleList = articleList.slice(0,cuttingIndex.value)
        break
    }
    
}
</script>

<style scoped>
@import '@/assets/font/font.css';
h1,h2,h4 {
    font-family: "hanna";
}
* {
    font-family: "hanna_air"
}

</style>