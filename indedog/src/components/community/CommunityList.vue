<template>
    <div>
        <h3>게시글 목록</h3>
        <select name="category" id="category" v-model="category">
            <option value="전체">전체</option>
            <option value="영화">영화</option>
            <option value="상영관">상영관</option>
            <option value="자유">자유</option>
            <option value="공지">공지</option>
        </select>
        <article v-for="article in store.articles"
        :key="article.id">
            <div v-if="article.category == category || category == '전체'">
                <h3>[{{ article.category }}]</h3>
                <p v-if="article.movie">({{ getMoviename(article.movie) }})</p>
                <RouterLink :to="{ name: 'CommunityDetailView', params: { id: article.id }}">
                    <h3>{{ article.title }}</h3>
                </RouterLink>
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
const getMoviename = function(movie_id) {
  // 배열에서 movie_id 키의 값이 매개변수 movieID와 일치하는 오브젝트를 찾습니다.
  const movie = store.movies.find(movie => movie.id === movie_id)
  return movie.title
}

</script>

<style scoped>
article {
    display: flex;
    flex-direction: row;
}
</style>