import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CinemaView from '@/views/CinemaView.vue'
import CinemaDetail from '@/components/CinemaDetail.vue'
import MovieSearch from '@/views/MovieSearch.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/cinema_list',
      name: 'cinema_list',
      component: CinemaView,
      children: [
        {path: 'detail', name: 'cinema_detail', component: CinemaDetail}
      ]
    },
    {
      path: '/movie_search',
      name: 'movie_search',
      component: MovieSearch
    }
  ]
})

export default router
