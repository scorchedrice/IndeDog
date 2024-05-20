<template>
    <div v-if="article">
        <h1>제목 : {{ article.title }}</h1>
        <h3>작성자 : {{ article.user }}</h3>
        <p>내용 : {{ article.content }}</p>
        <p>작성된 날짜 : {{ article.created_at }}</p>
        <p>수정된 날짜 : {{ article.updated_at }}</p>
        <div v-if="store.loginUser === article.user">
          <button @click="articleDelete(article.id)">
            게시글 삭제
          </button>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const router = useRouter()

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

const articleDelete = function(article_pk) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${article_pk}/update/`,
    headers: {
        Authorization : `Token ${store.token}`
    }
  })
    .then(res => {
      console.log('게시글 삭제 완료')
      router.replace({name: 'community'})
    })
    .catch(err => {
      console.log(err)
    })
  }


</script>

<style scoped>

</style>