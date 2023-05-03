<template>
    <div class="home w-full grow flex flex-col items-center lg:py-6">
        <div class="relative home-content lg:rounded-xl container z-40 grow flex flex-col max-w-screen-xl justify-between items-center gap-y-6"
            ref="target">
            <header class="container z-50 max-w-screen-xl">
                <HomeMenu></HomeMenu>
            </header>
            <main class="w-2/3 flex flex-col items-center justify-end gap-y-8 p-4 z-10">
                <div
                    class="relative rounded-full px-3 py-1 text-sm leading-6 text-neutral-200 ring-1 ring-neutral-600 hover:ring-neutral-500">
                    Announcing our App.
                    <a href="#" class="font-semibold text-fuchsia-500">Read more <span aria-hidden="true">&rarr;</span></a>
                </div>
                <h1 class="sm:text-center text-4xl font-bold tracking-tight text-neutral-50 sm:text-6xl">Create <span
                        class="text-fuchsia-300">a link</span> with your clients.
                </h1>
                <QrCodeIcon class="h-16 w-16 text-neutral-100 rotate-45" aria-hidden="true" />
                <p class="text-sm leading-6 text-neutral-300 text-center">
                    Communicate your care for your clients by utilizing our application.
                    Gather comprehensive contact and interaction histories.
                    Link any equipment your clients are using to provide prompt assistance in case of any unforeseen
                    circumstances.
                </p>
                <div class="mt-10 flex items-center justify-center gap-x-6">
                    <a href="#"
                        class="rounded-md bg-fuchsia-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-fuchsia-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-fuchsia-600">Get
                        started</a>
                    <a href="#" class="text-sm font-semibold leading-6 text-neutral-400">Learn more <span
                            aria-hidden="true">→</span></a>
                </div>
            </main>
            <footer
                class="parallax-container relative container w-full max-w-screen-xl flex justify-center items-end p-6 lg:px-8">
                <div class="w-1/2 z-10 flex flex-col gap-y-3 items-center">
                    <div class="text-xs">© 2023 LazyLab, Inc. All rights reserved.</div>
                    <SocialLinks></SocialLinks>
                </div>
                <!-- TODO: create composable from these -->
                <div class="home-parallax absolute inset-0">
                    <div class="parallax-layer" :style="layer0"></div>
                    <div class="parallax-layer" :style="layer1"></div>
                    <div class="parallax-layer" :style="layer2"></div>
                    <div class="parallax-layer" :style="layer3"></div>
                </div>
            </footer>
            <img class="decoration-bulb object-scale-down hidden lg:block" src="/home-parallax/decoration_0_1.png"
                alt="home-lightbulb">
        </div>
    </div>
</template>

<script lang="ts" setup>
import { computed, reactive, ref } from 'vue';
import { useParallax } from '@vueuse/core';

import { QrCodeIcon } from '@heroicons/vue/20/solid';

import SocialLinks from './SocialLinks.vue';
import HomeMenu from './Menu.vue';


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
        overflow: hidden;
        background-size: cover;
        background-position: center center;
        background-repeat: repeat;
        background-image: url("/home-parallax/grid_1.svg");
        background-color: #090809;
    }

    .parallax-container {
        height: 260px;
    }

    .decoration-bulb {
        position: absolute;
        top: 0;
        left: 14%;
        z-index: 55;
        width: auto;
        height: 10.5rem;
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
                background-image: url("/home-parallax/layer_0_1_small.png");
                z-index: 5;
            }

            &:nth-child(2) {
                background-image: url("/home-parallax/layer_0_2_small.png");
                z-index: 4;
            }

            &:nth-child(3) {
                background-image: url("/home-parallax/layer_0_3_small.png");
                z-index: 3;
            }

            &:nth-child(4) {
                background-image: url("/home-parallax/layer_0_4_small.png");
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