import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    linkActiveClass: 'active',
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('@/views/AboutView.vue')
        },
        {
            path: '/sahibin-cli',
            name: 'sahibin-cli',
            component: () => import('@/views/CLIView.vue')
        },
        {
            path: '/sahibin-api',
            name: 'sahibin-api',
            component: () => import('@/views/APIView.vue')
        },
        {
            path: '/share',
            name: 'share',
            component: () => import('@/views/ShareView.vue')
        },
        {
            path: '/:pathMatch(.*)',
            name: 'error',
            component: () => import('@/views/ErrorView.vue')
        }
    ]
})

export default router
