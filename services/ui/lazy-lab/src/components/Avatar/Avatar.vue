<template>
    <div class="avatar relative">
        <Badge label="Active"></Badge>
        <div class="w-full p-2.5 aspect-square rounded-full bg-cover bg-center bg-neutral-100"
            :style="{ backgroundImage: props.src ? `url(${props.src})` : 'unset' }">
            <svg v-show="!props.src" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1"
                class="fallback fill-neutral-300">
                <linearGradient id="avatar-gradient">
                    <stop offset="0%" stop-color="#00dbde90" />
                    <stop offset="100%" stop-color="#fc00ff90" />
                </linearGradient>

                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
            </svg>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { Badge } from '@/components/Badge';

const props = defineProps({
    src: {
        type: String,
        default: ''
    }
});

</script>
<style lang="scss" scoped>
.avatar {
    min-width: 44px;
    min-height: 44px;
    width: 3.4rem;
    aspect-ratio: 1;

    .fallback {
        stroke: url(#avatar-gradient);
    }
}
</style>
