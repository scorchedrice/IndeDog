<template>
    <div>
    <h1>게시글 작성</h1>

    <form @submit.prevent="updateArticle(articleId)">
      <div>
        <label for="category">카테고리 : </label>
        <select name="category" id="category" v-model="category">
        <option value="영화">영화</option>
        <option value="상영관">상영관</option>
        <option value="자유">자유</option>
        <option v-if="store.isStaff" value="공지">공지</option>
      </select>
      </div>
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="수정">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()
const articleId = ref(route.params.id)

const store = useCounterStore()
const API_URL = store.API_URL
const router = useRouter()
const article = ref(null)
const title = ref(null)
const content = ref(null)
const category = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${articleId.value}/`,
  })
    .then((response) => {
      console.log(response.data)
      article.value = response.data
      title.value = article.value.title
      content.value = article.value.content
      category.value = article.value.category
    })
    .catch((error) => {
      console.log(error)
    })
})

console.log(article.value)

const updateArticle = function(article_id) {
    axios({
      method: 'put',
      url: `${API_URL}/api/v1/articles/${article_id}/update/`,
      data: {
        title: title.value,
        content: content.value,
        category: category.value
      },
      headers: {
        Authorization : `Token ${store.token}`
      }
    })
    .then(res => {
      console.log(res)
      window.alert('게시글이 수정되었습니다.')
      router.replace({ name: 'CommunityDetailView', params: {'id': article_id}})
    })
    .catch(err => {
      console.log(err)
      window.alert('잘못된 입력입니다. 제목 또는 내용이 비어있는지 확인하세요.')
    })
  }


</script>

<style scoped>

</style>