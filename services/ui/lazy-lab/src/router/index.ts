import { createRouter, createWebHistory } from 'vue-router';
import { updateTitleGuard } from './guards';

const About = { template: '<div>About</div>' };

import { authRoute } from '../modules/auth/routes';


// Routes Declaration
export const routes = [
	{ path: '/about', component: About },
	// Home Section
	{ 
		path: '/home',
		component: () => import(/* webpackChunkName: 'home' */ '../modules/home/Home.vue'),
	},
	// Auth Section
	authRoute,

];


const router = createRouter({
	history: createWebHistory(),
	routes, // short for `routes: routes`
});

router.beforeEach(updateTitleGuard);
export default router;