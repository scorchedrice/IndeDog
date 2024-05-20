<template>
    <vue3-star-ratings
   v-model="rating"
   :starSize="32"
   starColor="#ff9800"
   inactiveColor="#333333"
   :numberOfStars="5"
   :disableClick="false"
    />
    <button @click="checkStar">평점 계산 시 사용</button>
</template>
  
<script setup>
import { defineComponent, ref } from "vue"
import vue3StarRatings from "vue3-star-ratings"
defineComponent({
    components: {
        vue3StarRatings
    }
})
const rating = ref(0)
// 아래는 평점 확인 용 임시 js
const checkStar = function () {
    console.log(rating.value)
}
</script>