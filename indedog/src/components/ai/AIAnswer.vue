<template>
    <div class="container">
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
  import { ref, defineProps, onMounted } from 'vue'
  import axios from 'axios'

  const props = defineProps({
    inputData: String
  })

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
            content: props.inputData,
            role: 'user',
          },],
          temperature: 0.3,
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
      console.log(props.inputData)
    } catch (error) {
      console.error('Error:', error)
      console.log(response)
      response.value = 'An error occurred while fetching the response.'
    } finally {
    console.log(response.value)
      loading.value = false
    }
  }

  onMounted(() =>{
    console.log(props.inputData),
    setTimeout(sendMessage, 3000)
  })
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