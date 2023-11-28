import LoginCheck from '@/views/LoginCheck.vue'
import MessageList from '@/views/MessageList.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'LoginCheck',
      component: LoginCheck
    },
    {
      path: '/messages',
      name: 'MessageList',
      component: MessageList
    }
  ]
})

export default router
