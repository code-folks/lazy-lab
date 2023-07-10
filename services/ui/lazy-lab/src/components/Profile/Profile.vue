<template>
  <div class="avatar-holder flex flex-col items-center gap-y-3">
    <Avatar></Avatar>
    <div class="flex flex-col items-center">
      <span class="text-neutral-700 font-semibold text-sm">{{ auth.user?.name }}</span>
      <span class="user-email text-neutral-400 text-xs">{{ auth.user?.email }}</span>
    </div>
    <div class="flex gap-x-4">
      <button
        className="px-2.5 py-2.5 text-neutral-600 duration-150 bg-neutral-100 rounded-lg hover:bg-fuchsia-100 active:bg-fuchsia-200">
        <Cog8ToothIcon class="h-6 w-6" aria-hidden="true" />
      </button>
      <button
        className="px-2.5 py-2.5 text-neutral-600 duration-150 bg-neutral-100 rounded-lg hover:bg-fuchsia-100 active:bg-fuchsia-200">
        <PowerIcon class="h-6 w-6" aria-hidden="true" />
      </button>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { useAuth } from '@/stores/auth';
import { Cog8ToothIcon, PowerIcon } from '@heroicons/vue/24/outline';

import { Avatar } from '@/components/Avatar';


const auth = useAuth();


</script>

