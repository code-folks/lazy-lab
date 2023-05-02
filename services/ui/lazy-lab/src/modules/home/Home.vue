<template>
    <div class="home w-full grow flex flex-col items-center py-6">
        <div class="relative home-content container z-40 grow flex flex-col max-w-screen-xl justify-between items-center gap-y-6"
            ref="target">
            <header class="container z-50 max-w-screen-xl">
                <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
                    <div class="flex lg:flex-1">
                        <a href="https://lazylab.solutions" class="-m-1.5 p-1.5">
                            <span class="sr-only">Lazy Lab</span>
                            <img class="h-12 w-auto" src="/logos/lazy-lab-logo-7-white.svg" alt="LazyLab Logo">
                        </a>
                    </div>

                    <div class="flex gap-x-12 text-neutral-50">
                        <a href="#" class="text-sm font-semibold leading-6 ">Our App</a>
                        <a href="#" class="text-sm font-semibold leading-6 ">Features</a>
                        <a href="#" class="text-sm font-semibold leading-6 ">Support</a>
                        <a href="#" class="text-sm font-semibold leading-6 ">About Us</a>
                    </div>
                    <div class="flex flex-1 lg:justify-end">
                        <router-link class="text-sm font-semibold leading-6" :to="{ name: 'auth:login' }">Log in <span
                                aria-hidden="true">&rarr;</span>
                        </router-link>
                    </div>
                </nav>
            </header>
            <main class="w-2/3 flex flex-col items-center justify-end gap-y-8 p-4 z-10">
                <div
                    class="relative rounded-full px-3 py-1 text-sm leading-6 text-neutral-200 ring-1 ring-neutral-600 hover:ring-neutral-500">
                    Announcing our new app.
                    <a href="#" class="font-semibold text-fuchsia-500">Read more <span aria-hidden="true">&rarr;</span></a>
                </div>
                <h1 class="text-4xl font-bold tracking-tight text-neutral-50 sm:text-6xl">Create link with your clients.
                </h1>
                <QrCodeIcon class="h-16 w-16 text-neutral-100 rotate-45" aria-hidden="true" />
                <p class="text-sm leading-6 text-neutral-300 text-center">
                    Let you clients know that you care about them. Gather full contact and interreaction history in our app.
                    Link devices with your clients and help them, if anything happends.
                </p>
                <div class="mt-10 flex items-center justify-center gap-x-6">
                    <a href="#"
                        class="rounded-md bg-fuchsia-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-fuchsia-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-fuchsia-600">Get
                        started</a>
                    <a href="#" class="text-sm font-semibold leading-6 text-neutral-400">Learn more <span
                            aria-hidden="true">→</span></a>
                </div>
            </main>
            <footer class="parallax-container shadow relative container w-full max-w-screen-xl isolate">
                <div class="home-parallax absolute inset-0">
                    <div class="parallax-layer" :style="layer0"></div>
                    <div class="parallax-layer" :style="layer1"></div>
                    <div class="parallax-layer" :style="layer2"></div>
                    <div class="parallax-layer" :style="layer3"></div>
                </div>
            </footer>
            <img class="decoration-bulb object-scale-down" src="/home-parallax/decoration_0_1.png" alt="home-lightbulb">
        </div>
    </div>
</template>

<script lang="ts" setup>
import { computed, reactive, ref } from 'vue';
import { useParallax } from '@vueuse/core';

import { QrCodeIcon } from '@heroicons/vue/20/solid';


const target = ref(null);
const parallax = reactive(useParallax(target));


const layer0 = computed(() => ({
    transform: `translateX(${parallax.tilt * 10}px) translateY(${parallax.roll * 10
        }px) scale(1.03)`,
}))
const layer1 = computed(() => ({
    transform: `translateX(${parallax.tilt * 20}px) translateY(${parallax.roll * 20
        }px) scale(1.03)`,
}))
const layer2 = computed(() => ({
    transform: `translateX(${parallax.tilt * 30}px) translateY(${parallax.roll * 30
        }px) scale(1.03)`,
}))
const layer3 = computed(() => ({
    transform: `translateX(${parallax.tilt * 40}px) translateY(${parallax.roll * 40
        }px) scale(1.03)`,
}))
</script>

<style lang="scss" scoped>
.home {
    .home-content {
        border-radius: 12px;
        overflow: hidden;
    }

    .container {
        background-color: #090809;
    }

    .parallax-container {
        height: 260px;
    }

    .decoration-bulb {
        position: absolute;
        top: 0;
        left: 128px;
        z-index: 55;
    }

    .home-parallax {
        overflow: visible;

        .parallax-layer {
            transition: .3s ease-out all;
            position: absolute;
            height: 100%;
            width: 100%;
            height: 640px;
            background-position: bottom;
            background-size: 100%;
            background-repeat: no-repeat;
            bottom: 0;

            &:nth-child(1) {
                background-image: url("/home-parallax/layer_0_1.png");
                z-index: 5;
            }

            &:nth-child(2) {
                background-image: url("/home-parallax/layer_0_2.png");
                z-index: 4;
            }

            &:nth-child(3) {
                background-image: url("/home-parallax/layer_0_3.png");
                z-index: 3;
            }

            &:nth-child(4) {
                background-image: url("/home-parallax/layer_0_4.png");
                z-index: 1;
            }
        }
    }
}

.hero-container {
    display: flex;
    flex-direction: column;
}
</style>