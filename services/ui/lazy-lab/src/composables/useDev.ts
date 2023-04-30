import { createSharedComposable, useToggle } from '@vueuse/core';
import { Ref } from 'vue'


interface useDevComposable {
    isDev: Ref<boolean>;
    toggleDev: Function;
    forceDev: Function;
}


export function $useDev(domainPattern: string = 'mock'): useDevComposable {
    const [isDev, toggleDev] = useToggle()

    function forceDev(){
        isDev.value = true;
    }

    let hostParts = window.location.hostname.split('.');
    if( hostParts.includes(domainPattern)) {
        isDev.value = true;
    }

    // expose managed state as return value
    return { 
        isDev,
        toggleDev,
        forceDev,
    }
}

const useDev = createSharedComposable($useDev);


export {
    useDev,
}