// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import CadastroView from '@/views/CadastroView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/cadastro',
    name: 'Cadastro',
    component: CadastroView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
