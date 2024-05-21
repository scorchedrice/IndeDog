<template>
    <div class="container">
      <h3>인공지능한테도 추천 받아보실래요?</h3>
      <textarea v-model="userInput" placeholder="Ask something..."></textarea>
      <button @click="sendMessage">Send</button>
      <div v-if="loading">Loading...</div>
      <div v-if="response">
        <h2>Response:</h2>
        <p>{{ response }}</p>
        <div class="container" style="margin: auto;">
        </div>
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

  const userInput = ref('')
  const response = ref('')
  const loading = ref(false)
  
  const sendMessage = async () => {
    loading.value = true
    response.value = ''
  
    try {
      const result = await axios.post(
        'https://api.openai.com/v1/chat/completions',
        {
        model: 'gpt-3.5-turbo',
          messages: [{
            content: userInput.value,
            role: 'user',
          },],
          temperature: 0.8,
          max_tokens: 500,
        },
        {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer sk-proj-Ng9Di9VUSWALCjTnftQUT3BlbkFJ66h9fBomsApfjKOQJw6V'
          }
        }
      )
      response.value = result.data.choices[0].message.content
      
    } catch (error) {
      console.error('Error:', error)
      console.log(response)
      response.value = 'An error occurred while fetching the response.'
    } finally {
    console.log(response.value)
      loading.value = false
    }
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