import Vue from 'vue'
import store from '@/store/index.js'
import router from '@/router/index.js'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPenSquare } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import axios from 'axios'

import VueAnalytics from 'vue-analytics'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL

library.add(faPenSquare)

Vue.component('font-awesome-icon', FontAwesomeIcon)

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
