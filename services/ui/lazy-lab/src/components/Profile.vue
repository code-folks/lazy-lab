<template>
  <Popover class="relative flex-initial">
    <PopoverButton>
      <div
        class="inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600">
        <!-- <span class="font-medium text-gray-600 dark:text-gray-300">JL</span> -->

        <svg v-if="!user" class="text-gray-400 -left-1 pt-2" fill="currentColor" viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path>
        </svg>

      </div>
    </PopoverButton>
    <PopoverPanel class="absolute left-1/2 z-10 mt-3 w-screen max-w-sm -translate-x-1/2 transform px-4 sm:px-0 lg:w-64 shadow">
      <div class="bg-white divide-y divide-neutral-100 rounded-lg dark:bg-gray-700 dark:divide-neutral-600">
        <div class="px-4 py-3 text-sm text-neutral-900 dark:text-white">
          <div>{{ 'Unknown' }}</div>
          <div class="font-medium truncate">{{  'no@email.yolo'}}</div>
        </div>
        <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="avatarButton">
          <li>
            <a href="#"
              class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Dashboard</a>
          </li>
          <li>
            <a href="#"
              class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Settings</a>
          </li>
        </ul>
        <div class="py-1">
          <a href="#"
            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Sign
            out</a>
        </div>
      </div>
    </PopoverPanel>
  </Popover>
</template>
<script lang="ts" setup>

import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import { useAuth } from '@/stores/auth';


const { user, isAuthenticated, isLoading } = useAuth();


</script>

