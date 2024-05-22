import { ref, onMounted } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const movies = ref([])
  const cinemas = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref()
  const filterMovies = ref()
  const token = ref(null)
  const loginUser = ref('')
  const loginPk = ref(null)
  const isStaff = ref(null)
  const isLoading = ref(true)
  const userData = ref(null)
  // const token = ref(null)
  // const isLogin = computed(() => {
  //   if (token.value === null) {
  //     return false
  //   } else{
  //     return true
  //   }
  // })

  onMounted(() => {
    isLoading.value = true
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
    })
      .then(res => {
        movies.value = res.data
        for(const movie of movies.value){
          movie.keywords = movie.keywords.split('#').filter(item => item.trim() !== '')
          movie.cinemas = movie.cinemas.split(',')
        }
        console.log('영화 데이터 불러옴')
        isLoading.value = false
      })
      .catch(err => console.log(err))
  
    })
    
    const getArticles = function () {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        // headers: {
        //   Authorization : `Token ${token.value}`
        // }
      })
        .then(response => {
          // console.log(response)
          console.log(response.data)
          articles.value = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
    
  const pwChange = function (payload) {
    console.log(payload)
    const { new_password1, new_password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      data: {
        new_password1, new_password2
      }
    })
      .then((res) => {
        console.log('비밀번호 변경성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    console.log(payload)
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        const password = password1
        logIn({username, password})
        window.alert('회원가입 성공')
        router.replace({ name: 'home'}).then(() => {
          window.location.reload()
          // menu 에 회원가입 이후 반영이 안되는 문제 해결, home page이동시에만 새로고침 활용
        })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function(payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 성공')
        token.value = res.data.key
        loginUser.value = username
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/admin/`,
        })
          .then(res => {
            for(const data in res.data){
              if (res.data[data].username === loginUser.value){
                if (res.data[data].is_staff) {
                  console.log('스태프입니다.')
                  isStaff.value = true
                }
                loginPk.value = res.data[data].id
                userData.value = res.data[data]
                break
              }
            }
          })
          .catch(err => {
            console.log(err)
          })
      })
      .catch((err) => {
        window.alert('로그인정보가 일치하지 않습니다.')
        console.log(err)  
        router.replace({ name: 'home'})
      })
  }

  const logOut = function() {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        console.log('로그아웃')
        token.value = null
        loginUser.value = null
        isStaff.value = false
        loginPk.value = null
        userData.value = null 
      })
      .catch((err) => {
        console.log(err)
      })
  }
        
  const getCoord = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/cinemas/`,
    })
    .then(res => {
      cinemas.value = res.data;
      console.log('#store - cinema')
      console.log(cinemas.value)
    })
    .catch(err => console.log(err))
  }
  

  return { movies, getArticles, API_URL, articles, signUp, logIn, token, loginUser, 
    getCoord, cinemas, logOut, isStaff, loginPk, isLoading, userData }
}, { persist: true })
