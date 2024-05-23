<template>
    <div style="border: solid black 5px;">
        <h1>모집합니다!</h1>
        <button @click.prevent="createJob">
            공고 작성
        </button>
    </div>
    <article class="row mt-2 g-4">
        <div class="col-12 col-md-6 col-lg-4" v-for="job in jobs" style="border: solid  2px;">
            <h2>{{ job.title }}</h2>
            <RouterLink :to="{ name: 'job_detail', params: { 'id': job.id }}">
                <button v-if="store.loginUser && store.loginUser != job.user && !check(job.applicant)" class="btn btn-dark" id="applicant">
                    지원하기
                </button>
                <button v-if="check(job.applicant)" class="btn btn-success" id="applicant">
                    등록완료/ 변경
                </button>
                <button v-if="store.loginUser == job.user" class="btn btn-info" id="applicant">
                    공고 수정
                </button>
            </RouterLink>
            <p>{{ job.by }}까지 | 모집분야 : {{ job.job }}</p>
            <br>
            <div class="d-flex">
            </div>
        </div>
    </article>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const jobs = ref(null)
const router = useRouter()

const check = function(applicant) {
    if (applicant) {
        if (applicant.includes(store.loginPk)){
            return true
        }
        return false
    } else {
        return false
    }
}

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
#applicant {
    position: flex;
}
</style>