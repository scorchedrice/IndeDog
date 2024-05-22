<template>
    <div>
        <h2>영화평론 (MovieCommunity)</h2>
        <!-- <select name="category" id="category" v-model="category">
            <option value="전체">전체</option>
            <option value="영화">영화</option>
            <option value="상영관">상영관</option>
            <option value="자유">자유</option>
            <option value="공지">공지</option>
        </select> -->
        <article v-for="article in store.articles"
        :key="article.id">
            <div v-if="article.category == '영화'" class="row">
                <!-- {{ article.movie }} -->
                <div class="col-8">
                    <RouterLink :to="{ name: 'CommunityDetailView', params: { id: article.id }}">
                        <h3>{{ article.title }}</h3>
                    </RouterLink>
                </div>
                <div class="col-4">
                    <h5>{{ article.user }}</h5>
                    <h6>{{ article.updated_at.slice(0,10) }}</h6>
                </div>
            <hr>
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
console.log(store.articles.length)
</script>

<style scoped>
</style>