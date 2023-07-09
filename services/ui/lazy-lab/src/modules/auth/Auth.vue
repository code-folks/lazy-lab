<template>
  <Bubbles :count=6 class="relative overflow-visible w-full h-full md:h-auto md:w-1/2 md:max-w-md grow md:grow-0">
    <div
      class="relative z-10 flex h-full items-center shadow justify-center rounded-lg bg-white px-8 py-16 sm:px-6 lg:px-12">
      <router-view></router-view>
    </div>

  </Bubbles>
</template>
  
<script lang="ts" setup>
import { Bubbles } from '@/components/Bubbles';

</script>

<style lang="scss">

</style>