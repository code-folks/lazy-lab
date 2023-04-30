<template>
  <router-view></router-view>
  <div v-if="isDev" class="dev-indicator shadow">
    <a href="/mock/">
      Powered by <span>MOCK</span>
    </a>
  </div>
</template>

<script lang="ts" setup>
import { useDev } from './composables';


const { isDev } = useDev("mock");

</script>

<style lang="scss">
.dev-indicator {
  color: #fff;
  position: absolute;
  top: 1.5rem;
  right: 0px;
  background: #111;
  width: auto;
  z-index: 40;
  padding: 0.42rem 0.6rem;
  font-size: 0.80rem;
  line-height: 1.1;
  font-weight: 200;
  border-bottom-left-radius: 12px;
  border-top-left-radius: 12px;
  span {
    font-weight: 500;
    font-size: 0.85rem;
    background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);
    background-clip: border-box;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
}
</style>