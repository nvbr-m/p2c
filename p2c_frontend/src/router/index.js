import Vue from 'vue';
import VueRouter from 'vue-router';
import compiler from '../views/compiler.vue';
import exercise from '../views/exercise.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/compiler',
    name: 'Compiler',
    component: compiler,
  },
  {
    path: '/',
    name: 'Home',
    component: exercise,
  },
  {
    path: '/:id',
    component: exercise,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
