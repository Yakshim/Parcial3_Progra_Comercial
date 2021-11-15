import Vue from 'vue'
import VueRouter from 'vue-router'

import Huesped from '@/components/Huesped'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/huespedes/lista',
    name: 'Huesped',
    component: Huesped
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router
