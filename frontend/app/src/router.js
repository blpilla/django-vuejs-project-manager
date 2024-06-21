import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/Login.vue';
import Clientes from './components/Clientes.vue';
import Projetos from './components/Projetos.vue';
import Atividades from './components/Atividades.vue';

const routes = [
  { path: '/login', component: Login },
  { path: '/clientes', component: Clientes },
  { path: '/projetos', component: Projetos },
  { path: '/atividades', component: Atividades },
  { path: '/:pathMatch(.*)*', redirect: '/login' }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const isAuthenticated = !!localStorage.getItem('token');

  if (authRequired && !isAuthenticated) {
    return next('/login');
  }

  next();
});

export default router;
