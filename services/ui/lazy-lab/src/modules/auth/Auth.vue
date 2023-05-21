<template>
  <Bubbles class="relative overflow-visible w-full h-full md:h-auto md:w-1/2 md:max-w-md grow md:grow-0">
    <div
      class="relative z-10 flex min-h-full items-center shadow justify-center rounded bg-white px-8 py-16 sm:px-6 lg:px-12">
      <div class="w-full grow max-w-md space-y-8">
        <div>
          <img class="mx-auto h-16 w-auto" src="/logos/lazy-lab-logo-7b.svg" alt="Your Company" />
          <h2 class="mt-6 text-center text-3xl font-bold tracking-tight text-zinc-800">Sign in to your account</h2>
        </div>
        <form class="mt-8 space-y-8" action="/mock/auth/login" method="POST">
          <input type="hidden" name="remember" value="true" />
          <div class="-space-y-px rounded-md shadow-sm">
            <div>
              <label for="username" class="sr-only">Email address</label>
              <input id="username" name="username" type="email" autocomplete="email" required="true"
                class="relative block w-full rounded-t-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-fuchsia-500 sm:text-sm sm:leading-6"
                placeholder="Email address" />
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input id="password" name="password" type="password" autocomplete="current-password" required="true"
                class="relative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-fuchsia-500 sm:text-sm sm:leading-6"
                placeholder="Password" />
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox"
                class="h-4 w-4 rounded border-gray-300 text-fuchsia-500 focus:ring-fuchsia-500" />
              <label for="remember-me" class="ml-2 block text-sm text-gray-900">Remember me</label>
            </div>

            <div class="text-sm">
              <router-link class="font-medium font-light text-zinc-500 hover:text-zinc-600" :to="{ name: 'auth:forgot' }">
                Forgot your password?
              </router-link>
            </div>
          </div>

          <div>
            <button type="submit"
              class="group relative flex w-full justify-center shadow-md rounded-md bg-zinc-950 px-3 py-2 text-sm font-semibold text-white hover:bg-zinc-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-zinc-800 hover:border-transparent">
              <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                <LockClosedIcon class="h-5 w-5 text-white" aria-hidden="true" />
              </span>
              Sign In with Email
            </button>
          </div>
        </form>
        <div class="relative">
          <div class="absolute inset-0 flex items-center"><span class="w-full border-t"></span></div>
          <div class="relative flex justify-center text-xs uppercase"><span
              class="bg-background px-2 text-zinc-600">Or continue with</span></div>
        </div>
        <div class="text-gray-900 text-sm text-center">
          Don't have an account ?
          <router-link class="text-fuchsia-600 hover:text-fuchsia-500" :to="{ name: 'auth:register' }">Create
            one</router-link>
        </div>
      </div>
    </div>

  </Bubbles>
</template>
  
<script lang="ts" setup>
import { PropType } from 'vue';
import { LockClosedIcon } from '@heroicons/vue/20/solid';

import { AuthAction } from './types';
import { useDev } from '../../composables';
import Bubbles from '../../components/Bubbles.vue';

const props = defineProps({
  action: {
    type: String as PropType<AuthAction>,
  }
});
const { isDev } = useDev();
console.log(isDev.value);

</script>

<style lang="scss">

</style>