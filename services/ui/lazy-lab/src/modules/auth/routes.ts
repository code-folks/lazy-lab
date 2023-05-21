import { RouteRecordRaw } from "vue-router";

export const authChildren: RouteRecordRaw[] = [
    {
		path: 'login',
		component: () => import(/* webpackChunkName: 'auth' */ './Login.vue'),
		name: 'auth:login',
		props: { action: 'login' },
		meta: { title: 'Sign in' }
	},
	{
		path: 'register',
		component: () => import(/* webpackChunkName: 'auth' */ './Register.vue'),
		name: 'auth:register',
		props: { action: 'register' },
		meta: { title: 'Sign up' }
	},
	{
		path: 'forgot',
		component: () => import(/* webpackChunkName: 'auth' */ './Forgot.vue'),
		name: 'auth:forgot',
		props: { action: 'forgot' },
		meta: { title: 'Recover access' }
	},
];

export const authRoute: RouteRecordRaw = {
    path: '/auth',
    component: () => import(/* webpackChunkName: 'auth' */ './Auth.vue'),
    children: authChildren,
    name: 'auth:home',
    props: { action: 'home' },
    meta: { title: 'Auth home' }
}

export default {
    authChildren,
    authRoute,
}
