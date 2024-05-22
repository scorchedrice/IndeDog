<template>  
      <div style="text-align: center;">
        
      
        <RouterLink :to="{name: 'ai_recommend'}">
            <img src="@/assets/icon/ai_icon.gif" alt="" style="width: 50px;">
        </RouterLink>
      </div>

      <h3 style="text-align: center;">AI가 오늘 추천하는 영화는 무엇일까요?</h3>
      
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import {RouterLink} from 'vue-router'
  import axios from 'axios'

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