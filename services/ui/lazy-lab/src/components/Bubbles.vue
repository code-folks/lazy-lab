<template>
    <div class="relative bubbles-container">
        <slot></slot>
        <div v-for="bubble in bubbles" :style="bubble.blockStyle" v-once>
            <img :src="bubble.src" :style="bubble.style">
        </div>
    </div>
</template>

<script setup lang="ts">
import { useBubbles } from '../composables/useBubbles';

const props = defineProps({
    count: {
        type: Number,
        default: 5,
    },
    zIndex: {
        type: Number,
        default: 1,
    }
});
const { bubbles } = useBubbles(props.count, props.zIndex);
</script>
<style lang="scss">
.bubbles-container {
    z-index: 10;
}
</style>
