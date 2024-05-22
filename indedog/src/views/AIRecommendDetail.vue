<template>
  <h3>4:완전 공감(이해)한다 <=> 1:공감(이해)하기 어렵다.</h3>
  <Carousel :itemsToShow="1.3" :wrapAround="true" :transition="500">
    <Slide v-for="slide in slides" :key="slide">
      <div class="carousel__item">
        <h1>{{ slide.title }}</h1>
        <h2>{{ slide.content }}</h2>
          <div v-for="select in slide.select_list">
            <button @click="pushPicked" :id="slide.id" type="button" class="btn">
              <h3 :id="slide.id">{{ select }}</h3>
              <p v-if="picked[slide.id]== select != ''">
                Checked!
              </p>
            </button>
          </div>
      </div>
    </Slide>

    <template #addons>
      <Navigation />
      <Pagination />
    </template>
  </Carousel>
  <div style="text-align: center;" v-if="cntPicked == 9">
    <button @click="calScore" type="button" class="btn" id="final">완료 하셨나요??</button>
  </div>
  <div v-if="showAns == true">
    <AIAnswer :input-data="inputData"/>
  </div>
  
</template>


<script setup>
import 'vue3-carousel/dist/carousel.css'
import {ref} from 'vue'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import AIAnswer from '@/components/AIAnswer.vue'

const picked=ref(['','','','','','','','','',''])
const four = ref([4,3,2,1])
const cntPicked = ref(0)
const showAns = ref(false)

const pushPicked = function (event) {
  picked.value[event.target.id] = event.target.innerText
  cntPicked.value = 0
  for (const pick of picked.value) {
    
    if (pick != '') {
      cntPicked.value++
      console.log(cntPicked.value)
    }
  }
  if (cntPicked.value === 9) {
    console.log('complete')
  }
}

const slides = [
  { id: 1, title: '나는', content: '청춘이라는 단어를 보면 가슴이 뛴다', select_list: four.value, target: '청춘'},
  { id: 2, title: '나는', content: '가족들과 함께 지내는 시간이 다른 것들 보다 소중하다', select_list: four.value, target: '가족'},
  { id: 3, title: '만약', content: '무서운 영화를 공짜로 볼 기회가 생긴다면', select_list: four.value, target: '공포'},
  { id: 4, title: '나는', content: '애니메이션을', select_list: four.value, target: 'animation'},
  { id: 5, title: '나는', content: '사랑의 힘을 굳게 믿는 사람이다.', select_list: four.value, target: '사랑'},
  { id: 6, title: '나는', content: '방황하는 청소년들을', select_list: four.value, target: '방황'},
  { id: 7, title: '만약', content: '나의 월급으로 노숙자 2명 평생의 끼니 및 거주 문제를 완벽하게 해결할 수 있다면 나는 기꺼이 월급을 지출할 것이다.', select_list: four.value, target: '취약층'},
  { id: 8, title: '나는', content: '과거의 역사에 관심이 있다.', select_list: four.value, target: '역사'},
  { id: 9, title: '나는', content: '지금 기분이', select_list: four.value, target: 'feel'},
]
// 점수 척도
// 1. 제거 여부를 판단할 변수
const inputData = ref('')
const favorite = ref([])
const like = ref([])
const hate = ref([])

const calScore = function() {
  console.log('calScore')
  inputData.value = ''
  favorite.value = []
  like.value = []
  hate.value = []
  for (const slide of slides) {
    
    if (picked.value[slide.id] == 4) {
      if (slide.target == 'feel') {
        inputData.value += '난 지금 기분이 매우 좋아'
      } else {
        favorite.value.push(slide.target)
      }
    } else if (picked.value[slide.id] == 3) {
      if (slide.target == 'feel') {
        inputData.value += '난 지금 기분이 좋은 편이야'
      } else {
        like.value.push(slide.target)
      }
    } else if (picked.value[slide.id] == 1) {
      if (slide.target == 'feel') {
        inputData.value += '난 지금 최악의 기분이야'
      } else {
        hate.value.push(slide.target)
      }
    }
  }
  if (favorite.value.length) {
    inputData.value += '내가 정말 정말 좋아하는 영화 키워드는 '
    for (const fav of favorite.value) {
      inputData.value += fav
      inputData.value += ' '
    }
    inputData.value += '이고'
  }
  if (hate.value.length != 0) {
    inputData.value += '내가 정말 싫어하는 영화 키워드는 '
    for (const hat of hate.value) {
      inputData.value += hat
      inputData.value += ' '
    }
    inputData.value += '이고'
  }
  if (like.value.length != 0) {
    inputData.value += '내가 조금은 좋아하는 키워드는 '
    for (const lik of like.value) {
      inputData.value += lik
      inputData.value += ' '
    }
  }
  inputData.value += '아무튼 독립영화를 보려고 하는데, 위 내용 기반으로 영화 키워드 추천해줘! 내 기분에 맞는 영화 장르를 추가로 추천해주고 내가 좋아하는 장르들 외에도 비슷한 것들 추가로 추천해줘!'
  console.log(inputData.value)
  showAns.value = true
}

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

<style>
.carousel__item {
  min-height: 500px;
  width: 100%;
  
  font-size: 20px;
  border: solid black 5px;
  border-radius: 8px;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 15px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
}
</style>
