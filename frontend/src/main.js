import Vue from 'vue'
import store from '@/store/index.js'
import router from '@/router/index.js'

import axios from 'axios'

import VueAnalytics from 'vue-analytics'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL

Vue.config.productionTip = false

// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
