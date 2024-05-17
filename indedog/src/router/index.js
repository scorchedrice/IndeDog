import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CinemaView from '@/views/CinemaView.vue'
import CinemaDetail from '@/components/CinemaDetail.vue'
import MovieSearchView from '@/views/MovieSearchView.vue'
import NowInTheaterView from '@/views/NowInTheaterView.vue'
import CommunityView from '@/views/CommunityView.vue'
import SignUp from '@/views/SignUp.vue'
import MovieDetail from '@/components/MovieDetail.vue'
import CinemaInfoView from '@/views/CinemaInfoView.vue'

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
      component: MovieSearchView
    },
    {
      path: '/movie_detail/:id',
      name: 'movie_detail',
      component: MovieDetail
    },
    {
      path: '/cinema_info/:address',
      name: 'cinema_info',
      component: CinemaInfoView,      
    },
    {
      path: '/now_in_theater',
      name: 'now_in_theater',
      component: NowInTheaterView,
      children: [
        {path: 'detail', name: 'now_cinema_detail', component: CinemaDetail}
      ]
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp,
      beforeEnter: (to, from, next) => {
        console.log('Enter')
        document.querySelector('#menu').style.display='none';
        next();
      },
    }
  ]
})
const menuHideEmit = function () {
  emit('menuHide')
}
export default router
