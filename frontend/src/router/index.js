import Vue from 'vue'
import VueRouter from 'vue-router'

import AddBlogPost from '@/components/AddBlogPost.vue'
import BlogPosts from '@/components/BlogPosts.vue'
import BlogPost from '@/components/BlogPost.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import PasswordReset from '@/views/PasswordReset.vue'
import store from '@/store/index.js'

const routes = [
  { path: '*', component: BlogPosts },
  { path: '/posts', component: BlogPosts },
  { path: '/posts/add', component: AddBlogPost, props: { action: 'add' } },
  { path: '/posts/edit/:slug', component: AddBlogPost, name: 'edit-post', props: { action: 'edit' } },
  { path: '/posts/read/:slug', component: BlogPost, name: 'read-post', props: true },
  { path: '/login', name: 'login', component: Login },
  { path: '/register', name: 'register', component: Register },
  { path: '/password-reset', name: 'password-reset', component: PasswordReset }
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

const authExcludedRoutes = [
  // Include Routes that SHOULD NOT check for authorization here
  'login',
  'register',
  'password-reset'
]

router.beforeEach((to, from, next) => {
  if (store.state.auth.loggedIn === false && !authExcludedRoutes.includes(to.name)) {
    next('/login')
  } else {
    next()
  }
})

export default router
