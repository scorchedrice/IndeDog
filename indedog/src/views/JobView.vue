<template>
    <div style="border: solid black 5px;">
        <h1>모집합니다!</h1>
        <button @click.prevent="createJob">
            공고 작성
        </button>
    </div>
    <article class="row">
        <div class="col-12 col-md-6 col-lg-4 g-3" v-for="job in jobs" style="border: solid  3px;">
            <h2>{{ job.title }}</h2>
            {{ job.by }}까지 | {{ job.job }}
        </div>
    </article>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const jobs = ref(null)
const router = useRouter()

const createJob = function () {
    router.push({ name: 'CommunityCreateView'})
}

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/job/`,
    })
      .then((res) => {
        jobs.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>

<style scoped>

</style>