<template>
    <template v-if="isloading">
        
    </template>
    <div v-if="!isloading">
        <h2>[{{ jobData.job }}] {{ jobData.title }}</h2>
        <h4>~ {{ jobData.by }}</h4>
        <hr>
        <hr>
        <h5>{{ jobData.content }}</h5>
        <h6>작성일 : {{ jobData.created_at.slice(0,10) }}</h6>
        <button v-if="store.loginUser && store.loginUser != jobData.user && !isSubmit" class="btn btn-primary" @click.prevent="submitApp(1)">
            지원넣기
        </button>
        <button v-if="isSubmit" class="btn btn-warning" @click.prevent="submitApp(2)">
            지원취소
        </button>
        <button v-if="store.loginUser == jobData.user" class="btn btn-danger" @click.prevent="deleteApp">
            공고 내리기
        </button>
        <button v-if="store.loginUser == jobData.user" class="btn btn-primary" @click.prevent="updateApp">
            공고 수정
        </button>
        <h2>
            <template v-if="store.loginUser == jobData.user">
                지원현황 : {{ applicant.length }}
                <div v-for="person in applicantName">
                    <RouterLink :to="{ name: 'userpage', params: {'username' : person}}">
                        <h1>{{ person }}</h1>
                    </RouterLink>
                </div>
            </template>
        </h2>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

const isloading = ref(true)
const router = useRouter()
const store = useCounterStore()
const route = useRoute()
const jobId = ref(route.params.id)
const jobData = ref([])
const applicant = ref([])
const applicantName = ref([])
const isSubmit = ref(false)


onMounted (() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/job/detail/${jobId.value}/`,
    })
      .then((res) => {
        console.log(res.data)
        jobData.value = res.data
        if (jobData.value.applicant) {
            applicant.value = jobData.value.applicant
        }
        
        applicantName.value = []
        for (const person of applicant.value){
            for (const user of store.userList) {
                if (person == user.id){
                    applicantName.value.push(user.username)
                    break
                }
                if (person == store.loginPk)
                { isSubmit.value = true}
            }
        }
        console.log(applicantName.value)
        isloading.value = false
      })
      .catch((err) => {
        console.log(err)
      })
})


const submitApp = function (type) {
    if (type == 1) {
        applicant.value.push(store.loginPk)
        isSubmit.value = true
    } else {
        applicant.value = applicant.value.filter(user => user !== store.loginPk)
        isSubmit.value = false
    }
    axios({
        method: 'put',
        url: `${store.API_URL}/api/v1/articles/job/update/${jobId.value}/`,
        data: {
            applicant: applicant.value
        },
        headers: {
        Authorization : `Token ${store.token}`
      }
    })
      .then((res) => {
        jobData.applicant = applicant.value
        if (res.data.applicant.includes(store.loginPk)) {
            window.alert('지원완료')
        } else {
            window.alert('지원취소 완료')
        }
        router.replace({name: 'job'})
      })
      .catch((err) => {
        console.log(err)
      })
}


const deleteApp = function () {
    axios({
        method: 'delete',
        url: `${store.API_URL}/api/v1/articles/job/update/${jobId.value}/`,
        headers: {
        Authorization : `Token ${store.token}`
      }
    })
      .then((res) => {
        window.alert('공고 삭제 완료')
        router.replace({name: 'job'})
      })
      .catch((err) => {
        console.log(err)
      })
}


const updateApp = function() {
    router.push({ name: 'job_update', params: { 'id': jobId.value }})
}

</script>

<style scoped>

</style>