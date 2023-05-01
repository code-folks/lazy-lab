import { createRouter, createWebHistory } from 'vue-router';
import { updateTitleGuard } from './guards';

const Home = { template: '<div>Home</div>' };
const About = { template: '<div>About</div>' };


// Routes Declaration
export const routes = [
	{ path: '/', component: Home },
	{ path: '/about', component: About },
	// Auth Section
	{
		path: '/auth/login',
		component: () => import(/* webpackChunkName: 'auth' */ '../modules/auth/Auth.vue'),
		name: 'auth:login',
		props: { action: 'login' },
		meta: { title: 'Sign in' }
	},
	{
		path: '/auth/register',
		component: () => import(/* webpackChunkName: 'auth' */ '../modules/auth/Auth.vue'),
		name: 'auth:register',
		props: { action: 'register' },
		meta: { title: 'Registration' }
	},
	{
		path: '/auth/forgot',
		component: () => import(/* webpackChunkName: 'auth' */ '../modules/auth/Auth.vue'),
		name: 'auth:forgot',
		props: { action: 'forgot' },
		meta: { title: 'Recover access' }
	},
];


const router = createRouter({
	history: createWebHistory(),
	routes, // short for `routes: routes`
});

router.beforeEach(updateTitleGuard);
export default router;