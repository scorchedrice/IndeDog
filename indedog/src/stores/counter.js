import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])
  const cinemas = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
    })
      .then(res => {
        console.log(res.data)
        movies.value = res.data
      })
      .catch(err => console.log(err))
    }
  
  const getCoord = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/cinemas/`,
    })
      .then(res => {
        cinemas.value = res.data;
        console.log('#store - cinema')
      })
      .catch(err => console.log(err))
  }
  
  return { movies, getMovies, getCoord, cinemas }
}, { persist: true })
