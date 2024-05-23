<template>
    <div>
        <h2>자유 주제라능~</h2>
        <article v-for="article in store.articles"
        :key="article.id">
        <div v-if="article.category == '자유'" class="row">
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
</script>

<style scoped>
</style>