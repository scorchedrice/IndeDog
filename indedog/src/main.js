import { createApp } from 'vue'
import { createPinia } from 'pinia'


import '../node_modules/flowbite-vue/dist/index.css'

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'

// star rating
import vue3StarRatings from "vue3-star-ratings"
// popover
import 'wowerlay/style.css'

const pinia = createPinia()
const app = createApp(App)

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)
app.use(router)
app.component("vue3-star-ratings", vue3StarRatings)
app.mount('#app')
