<template>
    <main>
  <div>
    <header class="pb-3 mb-4 border-bottom">
      <div class="body-tertiary rounded-3">
        <div class="container-fluid">
          <img src="@/assets/icon/ai_icon.gif" alt="" style="width: 30px;">
          <h1 class="display-5 fw-bold">당신의 취향에 맞는 영화를 추천해드릴게요!</h1>
        </div>
      </div>
    </header>
    <div class="row align-items-md-stretch">
      <div class="col-md-6">
        <div class="h-100 p-5 text-bg-dark rounded-3">
          <h3>편하게 선택하세요</h3>
          <br>
          <p>제가 여러가지 질문을 드리면, 이에 대한 생각을 선택지를 통해 제게 알려주세요.</p>
          <br>
          <h3>질문마다 1부터 4가 적힌 선택지를 드려요.</h3>
          <p>제가 드린 질문이 마음에 들거나 공감(혹은 이해)한다면 높은 숫자를 선택해주시고,</p>
          <p>질문이 마음에 들지 않거나 공감(혹은 이해)하기 어렵다면 낮은 숫자를 선택해주세요.</p>
        </div>
      </div>
      <div class="col-md-6">
        <div class="h-100 p-5 bg-body-tertiary border rounded-3">
          <h3>Example</h3>
          <br>
          <h5>예시. 친구가 평양냉면을 먹으러 가자고 권유한다면 나는</h5>
          <hr>
          <p>- 왜 이제서야 말한거야! 너도 좋아하니? 여기 앞에 내가 가장 .. => 4</p>
          <p>- 어? 오늘 일찍 끝나면 집가는 길에 한번 가자 => 3</p>
          <p>- 엥? 난 아직 맛을 잘 몰라서.. => 2</p>
          <p>- 도대체 걸레빤물을 왜 먹는거야 => 1</p>
          <button class="btn btn-outline-secondary" type="button"
          @click="goAI">준비되셨으면 가볼까요?</button>
        </div>
      </div>
    </div>

    <footer class="pt-3 mt-4 text-body-secondary border-top">
      © 2024
    </footer>
  </div>
</main>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const goAI = function () {
  router.push({name: 'ai_recommend'})
}

</script>

<style scoped>

</style>