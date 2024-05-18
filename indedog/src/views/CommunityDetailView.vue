<template>
    <div v-if="article">
        <h1>제목 : {{ article.title }}</h1>
        <h3>작성자 : {{ article.user }}</h3>
        <p>내용 : {{ article.content }}</p>
        <p>작성된 날짜 : {{ article.created_at }}</p>
        <p>수정된 날짜 : {{ article.updated_at }}</p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      console.log(response.data)
      article.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})


</script>

<style scoped>

</style>