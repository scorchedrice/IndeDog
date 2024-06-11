<template>
    <form @submit.prevent="updateArticle">
        <div>
            구인공고를 작성해주세요.
        </div>
        <div>
            <label for="title">제목 : </label>
            <input type="text" v-model.trim="title" id="title">
        </div>
        <div>
            <label for="content">내용 : </label>
            <textarea v-model.trim="content" id="content"></textarea>
        </div>
            <label for="job">모집부문 : </label>
            <input type="text" v-model.trim="job" id="job">
            <label for="by">지원 마감기한 : </label>
            <input type="date" v-model="by" id="by">
        <input type="submit">
    </form>
</template>

<script setup>
// job/article/update/<int:job_pk>/

import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const title = ref('')
const content = ref('')
const job = ref('')
const by = ref('')
const articleId = ref(route.params.id)
const article = ref(null)
const router = useRouter()

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/job/detail/${articleId.value}/`,
  })
    .then((response) => {
      article.value = response.data
      title.value = article.value.title
      content.value = article.value.content
      job.value = article.value.job
      by.value = article.value.by
    })
    .catch((error) => {
      console.log(error)
    })
})

const updateArticle = function() {
    axios({
      method: 'put',
      url: `${store.API_URL}/api/v1/articles/job/article/update/${articleId.value}/`,
      data: {
        title: title.value,
        content: content.value,
        job: job.value,
        by: by.value
      },
      headers: {
        Authorization : `Token ${store.token}`
      }
    })
    .then(res => {
      console.log(res)
      window.alert('게시글이 수정되었습니다.')
      router.replace({ name: 'job_detail', params: {'id': articleId.value}})
    })
    .catch(err => {
      console.log(err)
      window.alert('잘못된 입력입니다. 제목 또는 내용이 비어있는지 확인하세요.')
    })
}

</script>

<style scoped>

</style>