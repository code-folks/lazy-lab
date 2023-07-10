<template>
<span 
    class="badge absolute border border-2 border-white bg-teal-400 z-5" 
    :style="{ [props.x]: '0.25rem', [props.y]: '-0.25rem', 'height': props.size + 'px', 'aspectRatio': 1, 'borderRadius': props.size + 'px' }"
    :class="{ 'typing': typing}" :title="props.label"
>
</span>    
</template>

<script lang="ts" setup>
import { PropType, toRef, ref } from 'vue';

const props = defineProps({
    x: {
        type: String as PropType<'left' | 'right'>,
        default: 'right'
    },
    y: {
        type: String as PropType<'top' | 'bottom'>,
        default: 'bottom'
    },
    size: {
        type: Number,
        default: 13
    },
    typing: {
        typing: Boolean,
        default: false
    },
    label: {
        typing: String,
        default: ""
    }
})

const typing = toRef(props, 'typing')
</script>
<style lang="scss" scoped>
.typing {
    animation: 3.8s ease-in-out 100ms infinite jump ;
}

</style>
