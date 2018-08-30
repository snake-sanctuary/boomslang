import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/components/Login'
import Profile from '@/components/Profile'
import Signup from '@/components/Signup'
import NotFoundComponent from '@/components/NotFoundComponent'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }, {
      path: '/login/',
      name: 'login',
      component: Login
    }, {
      path: '/signup/',
      name: 'signup',
      component: Signup
    }, {
      path: '/profile/',
      name: 'profile',
      component: Profile
    }, {
      path: '*',
      component: NotFoundComponent
    }
  ]
})
