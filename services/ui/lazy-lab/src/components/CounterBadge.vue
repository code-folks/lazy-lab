<template>
    <div v-show="badgeVisible" ref="targetBadge"
        class="badge absolute -top-0.5 -right-1 w-5 h-5 grid place-items-center tabular-nums text-neutral-50 rounded-full bg-fuchsia-400">
        {{ badgeCounter }}
    </div>
</template>

<script setup lang="ts">
import { ref, computed, toRefs, watch } from 'vue'
import { useMotion } from '@vueuse/motion';

const props = defineProps({
    count: {
        type: Number,
        default: 0,
    },

});
const { count } = toRefs(props);
const targetBadge = ref<HTMLElement | null>(null);
const badgeVisible = computed(() => count.value > 0);
const badgeCounter = computed(() => count.value > 99 ? '🏅' : count.value )
const motionInstance = useMotion(targetBadge, {
    initial: {
        opacity: 0,
        scale: 0.1,
    },
    enter: {
        opacity: 1,
        scale: 1.2,
    },
    visibleOnce: {
        opacity: 1,
        scale: 1,
        y: 0
    },
    leave: {
        opacity: 0,
        scale: 0,
    },
    pulse: {
        y: -3
    }
})

watch(count, (next, prev) => {
    motionInstance.apply('pulse')?.then(
        () => motionInstance.apply('visibleOnce')
    )
});


</script>
<style lang="scss">
.badge {
    font-size: 0.7rem;
    line-height: 0.8rem;
}

</style>
