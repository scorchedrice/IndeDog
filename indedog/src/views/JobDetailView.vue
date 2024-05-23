<template>
    <div>
        <h1>제목 : {{ title2 }}</h1>
        <hr>
        <p>
            모집분야 : {{ job2 }}
        </p>
        <h2>내용 : {{ content2 }}</h2>
        <h4>작성일 : {{ date }}</h4>
        <button v-if="store.loginUser && store.loginUser != writer && !isSubmit" class="btn btn-primary" @click.prevent="submitApp(1)">
            지원넣기
        </button>
        <button v-if="isSubmit" class="btn btn-warning" @click.prevent="submitApp(2)">
            지원취소
        </button>
        <button v-if="store.loginUser == writer" class="btn btn-danger" @click.prevent="deleteApp">
            공고 내리기
        </button>
        <button v-if="store.loginUser == writer" class="btn btn-primary" @click.prevent="updateApp">
            공고 수정
        </button>
        <h2 v-if="applicant.length">
            지원현황 : {{ applicant.length }}
            <template v-if="store.loginUser == writer">
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
import moment from 'moment'

const router = useRouter()
const store = useCounterStore()
const route = useRoute()
const jobId = ref(route.params.id)
const jobData = ref()
const applicant = ref([])
const applicantName = ref([])
const isSubmit = ref(false)
const title2 = ref('')
const content2 = ref('')
const job2 = ref('')
const writer = ref('')
const date = ref('')

onMounted (() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/job/detail/${jobId.value}/`,
    })
      .then((res) => {
        jobData.value = res.data
        const { title, content, job, created_at } = jobData.value
        title2.value = title
        content2.value = content
        job2.value = job
        writer.value = jobData.value.user
        if (jobData.value.applicant) {
            applicant.value = jobData.value.applicant
        }
        moment.locale('ko')
        date.value = moment(created_at).format('YYYY년 MM월 DD일 HH:mm')
        if (jobData.value.applicant && jobData.value.applicant.includes(store.loginPk)) {
            isSubmit.value = true
        } else {
            isSubmit.value = false
        }
        applicantName.value = []
        for (const person of applicant.value){
            for (const user of store.usersData) {
                if (person == user.id){
                    applicantName.value.push(user.username)
                    break
                }
            }
        }
        console.log(applicantName.value)
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