<template>
    <div class="container">
      <h3>인공지능한테도 추천 받아보실래요?</h3>
        <div class="container" style="margin: auto;">
            <RouterLink :to="{name: 'ai_recommend'}">
                <img src="@/assets/icon/AI_icon.webp" alt="" style="width: 50%;" @click="clickAI">
            </RouterLink>
        </div>
      </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import {RouterLink} from 'vue-router'
  import axios from 'axios'
  
  
  const clickAI = function () {
    console.log('clickAI')
  }
  </script>
  
  <style>
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 10px;
  }
  button {
    display: block;
    margin-bottom: 10px;
  }
  </style>