




<template>
  <div>
    <div>
      <div style="text-align: center; margin-top: 20px;">
        <RouterLink :to="{name: 'home'}">
          <img src="@/assets/icon/site_icon_1.jpg" class="rounded col" alt="Home" width="100px" height="100px">
        </RouterLink>
      </div>
    </div>
    <div style="position: fixed; top: 80px; left: 80px;">
      <img src="@/assets/icon/site_icon_1.jpg" class="rounded col" alt="Home" width="100px" height="100px" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">

      <div class="offcanvas offcanvas-start" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasWithBothOptionsLabel">Backdrop with scrolling</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
      <div class="offcanvas-body">
        <ul class="list-group list-group-flush">
          <div class = "accordion" id="login">
            <h2 class="accordion-header">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                로그인 / 회원가입
              </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
              <div class="accordion-body">
                <strong>로그인인 경우, 이를 출력하지 않습니다.</strong>
              </div>
            </div>
          </div>
          <li class="list-group-item">작품 검색</li>
          <li class="list-group-item">상영관 검색</li>
          <li class="list-group-item">현재 상영작</li>
          <li class="list-group-item">커뮤니티</li>
        </ul>
      </div>
    </div>
  </div>
    
  <div style="width: fit-content; text-align: center;">
    <RouterView />
  </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>