import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useAuthStore } from '@/stores/auth'
import { useSearchStore } from '@/stores/search'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: '/login',
      component: () => import('../views/LoginView.vue'),
      children: []
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue')
    },
    {
      path: '/article/:id',
      name: 'article',
      component: () => import('../views/ArticleView.vue'),
      props: true,
      beforeEnter(to, from, next) {
        const search = useSearchStore()
        const article = search.getArticleById(Number(to.params.id))
        if (article) {
          to.params.article = article
          next()
        } else {
          next({ name: 'dashboard' })
        }
      }
    }
  ]
})

router.beforeEach(async (to) => {
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  const user = useUserStore()
  const auth = useAuthStore()

  if (authRequired && !user.user) {
    auth.returnUrl = to.fullPath
    return '/login'
  }
})

export default router
