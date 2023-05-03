<template>
    <nav class="flex items-center justify-between p-6 lg:px-8 gap-x-8" aria-label="Global">
        <div class="flex lg:flex-1">
            <a href="https://lazylab.solutions" class="-m-1.5 p-1.5">
                <span class="sr-only">Lazy Lab</span>
                <img class="h-12 w-auto" src="/logos/lazy-lab-logo-7-white.svg" alt="LazyLab Logo">
            </a>
        </div>
        <div class="flex gap-x-12 text-neutral-50 flex-wrap">
            <a href="#" class="text-sm hover:text-fuchsia-300 font-semibold leading-6 ">Our App</a>
            <a href="#" class="text-sm hover:text-fuchsia-300 font-semibold leading-6 ">Features</a>
            <a href="#" class="text-sm hover:text-fuchsia-300 font-semibold leading-6 ">Support</a>
            <a href="#" class="text-sm hover:text-fuchsia-300 font-semibold leading-6 ">About Us</a>
        </div>
        <div class="flex lg:flex-1 justify-end">
            <router-link class="text-sm font-semibold text-neutral-50 hover:text-fuchsia-300 leading-6" :to="{ name: 'auth:login' }">Log in <span
                    aria-hidden="true">&rarr;</span>
            </router-link>
        </div>
    </nav>
</template>

<script lang="ts" setup>

</script>

<style lang="scss" scoped></style>