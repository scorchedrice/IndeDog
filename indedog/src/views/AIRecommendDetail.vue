<script setup>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

const slides = [
  { id: '1', title: 'Vue 3 Introduction', content: 'VueJS is a library' },
  { id: '2', title: 'Vue 3 Components', content: 'Know the components' },
  { id: '3', title: 'Vue 3 Conditional', content: 'Rendering Conditionally' },
  { id: '4', title: 'Vue 3 Reactivity', content: 'VueJS is Reactive' },
  { id: '5', title: 'Vue 3 Compute', content: 'VueJS uses computed properties' },
]

const breakpoints = {
  // 700px and up
  700: {
    itemsToShow: 2,
    snapAlign: 'center',
  },
  // 1024 and up
  1024: {
    itemsToShow: 2,
    snapAlign: 'start',
  },
}
</script>

<template>
  <Carousel :wrap-around="true" :breakpoints="breakpoints" :autoplay="2000">
    <Slide v-for="slide in slides" :key="slide.id">
      <div class="carousel__item">
        <h3>{{ slide.title }}</h3>
        <p>{{ slide.content }}</p>
      </div>
    </Slide>

    <template #addons>
      <Navigation />
      <Pagination />
    </template>
  </Carousel>
</template>

<style>
.carousel__item {
  min-height: 200px;
  width: 100%;
  background-color: var(--vc-clr-primary);
  color: var(--vc-clr-white);
  font-size: 20px;
  border-radius: 8px;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}
</style>
