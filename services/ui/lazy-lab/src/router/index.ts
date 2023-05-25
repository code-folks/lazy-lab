import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import { updateTitleGuard } from './guards';

const About = { template: '<div>About</div>' };

import { authRoute } from '../modules/auth/routes';


// Routes Declaration
export const routes: RouteRecordRaw[] = [
	{ path: '/about', component: About },
	// Home Section
	{ 
		path: '/home',
		component: () => import(/* webpackChunkName: 'home' */ '../modules/home/Home.vue'),
	},
	// Auth Section
	authRoute,
	{
		path: '/app',
		component: () => import(/* webpackChunkName: 'home' */ '../layouts/shell/Shell.vue'),
		name: 'shell'
	}
];


const router = createRouter({
	history: createWebHistory(),
	routes, // short for `routes: routes`
});

router.beforeEach(updateTitleGuard);
export default router;