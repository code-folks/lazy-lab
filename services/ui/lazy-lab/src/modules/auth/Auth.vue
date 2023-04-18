<template>
  <div class="relative container overflow-visible">
    <div
      class="relative z-10 flex min-h-full items-center shadow justify-center rounded bg-white px-8 py-16 sm:px-6 lg:px-12">
      <div class="w-full max-w-md space-y-8">
        <div>
          <img class="mx-auto h-16 w-auto" src="/logos/lazy-lab-logo-7.svg" alt="Your Company" />
          <h2 class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">Sign in to your account</h2>
        </div>
        <form class="mt-8 space-y-8" action="#" method="POST">
          <input type="hidden" name="remember" value="true" />
          <div class="-space-y-px rounded-md shadow-sm">
            <div>
              <label for="email-address" class="sr-only">Email address</label>
              <input id="email-address" name="email" type="email" autocomplete="email" required="true"
                class="relative block w-full rounded-t-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Email address" />
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input id="password" name="password" type="password" autocomplete="current-password" required="true"
                class="relative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Password" />
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox"
                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
              <label for="remember-me" class="ml-2 block text-sm text-gray-900">Remember me</label>
            </div>

            <div class="text-sm">
              <a href="#" class="font-medium text-zinc-700 hover:text-zinc-600">Forgot your password?</a>
            </div>
          </div>

          <div>
            <button type="submit"
              class="group relative flex w-full justify-center shadow-md rounded-md bg-zinc-950 px-3 py-2 text-sm font-semibold text-white hover:bg-zinc-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-zinc-800 hover:border-transparent">
              <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                <LockClosedIcon class="h-5 w-5 text-white" aria-hidden="true" />
              </span>
              Sign in
            </button>
          </div>
        </form>
      </div>
    </div>
    <div class="hidden md:block bubble-container absolute h-8 w-8 top-4 left-8">
      <img class="bubble" src="/img/bubble-2.svg">
    </div>
    <div class="hidden md:block bubble-container absolute h-10 w-10 top-4 right-2">
      <img class="bubble" src="/img/bubble-2.svg">
    </div>
    <div class="hidden md:block bubble-container absolute h-16 w-16 top-4 left-24">
      <img class="bubble" src="/img/bubble-3.svg">
    </div>
    <div class="hidden md:block bubble-container absolute h-6 w-6 top-4 right-36">
      <img class="bubble" src="/img/bubble-4.svg">
    </div>
    <div class="hidden md:block bubble-container absolute h-8 w-8 top-4 right-12">
      <img class="bubble" src="/img/bubble-4.svg">
    </div>
  </div>
</template>
  
<script lang="ts" setup>
import { LockClosedIcon } from '@heroicons/vue/20/solid'
</script>

<style lang="scss">
.bubble {
  z-index: 1;
  animation: wobble 4.09s 425ms infinite;
  &:nth-of-type(2) {
    animation: wobble 4.56s 121ms infinite;
  }
  &:nth-of-type(3) {
    animation: wobble 3.63s 211ms infinite;
  }
  &:nth-of-type(4) {
    animation: wobble 4.71s 151ms infinite;
  }
  &:nth-of-type(5) {
    animation: wobble 3.89s 243ms infinite;
  }
  &:nth-of-type(6) {
    animation: wobble 2.88s 107ms infinite;
  }
}

.bubble-container {
  overflow-y: visible;
  &:nth-of-type(2) {
    animation: up 5.73s 282ms infinite;
  }

  &:nth-of-type(3) {
    animation: up 4.12s 150ms infinite;
  }

  &:nth-of-type(4) {
    animation: up 5.03s 348ms infinite;
  }

  &:nth-of-type(5) {
    animation: up 4.33s 1.25s infinite;
  }

  &:nth-of-type(6) {
    animation: up 3.57s 210ms infinite;
  }
}

@keyframes wobble {

  33% {
    transform: translateX(-48px);
  }

  66% {
    transform: translateX(48px);
  }

}

@keyframes up {

  0% {
    opacity: 0;
  }

  40%,
  80% {
    opacity: 1;
  }

  100% {
    opacity: 0;
    transform: translateY(-680px);
  }

}</style>