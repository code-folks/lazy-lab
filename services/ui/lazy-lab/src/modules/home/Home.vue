<template>
    <div class="home w-full grow flex flex-col items-center lg:py-6">
        <div class="relative home-content lg:rounded-xl container z-40 grow flex flex-col max-w-screen-xl justify-between items-center gap-y-6"
            ref="target">
            <header class="container z-50 max-w-screen-xl">
                <nav class="flex items-center justify-between p-6 lg:px-8 gap-x-8" aria-label="Global">
                    <div class="flex lg:flex-1">
                        <a href="https://lazylab.solutions" class="-m-1.5 p-1.5">
                            <span class="sr-only">Lazy Lab</span>
                            <img class="h-12 w-auto" src="/logos/lazy-lab-logo-7-white.svg" alt="LazyLab Logo">
                        </a>
                    </div>

                    <div class="flex gap-x-12 text-neutral-50 flex-wrap">
                        <a href="#" class="text-sm font-semibold leading-6 ">Our App</a>
                        <a href="#" class="text-sm font-semibold leading-6 ">Features</a>
                        <a href="#" class="text-sm font-semibold leading-6 ">Support</a>
                        <a href="#" class="text-sm font-semibold leading-6 ">About Us</a>
                    </div>
                    <div class="flex lg:flex-1 justify-end">
                        <router-link class="text-sm font-semibold leading-6" :to="{ name: 'auth:login' }">Log in <span
                                aria-hidden="true">&rarr;</span>
                        </router-link>
                    </div>
                </nav>
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
                <div class="w-1/2 z-10 flex flex-col gap-y-2 items-center">
                    <div class="text-xs">© 2023 LazyLab, Inc. All rights reserved.</div>
                    <div class="text-zinc-300 flex gap-x-3">
                        <a href="https://github.com/code-folks/lazy-lab" class="hover:text-fuchsia-200">
                            <svg class=" fill-current" width="24" height="24" viewBox="0 0 64 64">
                                <path
                                    d="M32 1.7998C15 1.7998 1 15.5998 1 32.7998C1 46.3998 9.9 57.9998 22.3 62.1998C23.9 62.4998 24.4 61.4998 24.4 60.7998C24.4 60.0998 24.4 58.0998 24.3 55.3998C15.7 57.3998 13.9 51.1998 13.9 51.1998C12.5 47.6998 10.4 46.6998 10.4 46.6998C7.6 44.6998 10.5 44.6998 10.5 44.6998C13.6 44.7998 15.3 47.8998 15.3 47.8998C18 52.6998 22.6 51.2998 24.3 50.3998C24.6 48.3998 25.4 46.9998 26.3 46.1998C19.5 45.4998 12.2 42.7998 12.2 30.9998C12.2 27.5998 13.5 24.8998 15.4 22.7998C15.1 22.0998 14 18.8998 15.7 14.5998C15.7 14.5998 18.4 13.7998 24.3 17.7998C26.8 17.0998 29.4 16.6998 32.1 16.6998C34.8 16.6998 37.5 16.9998 39.9 17.7998C45.8 13.8998 48.4 14.5998 48.4 14.5998C50.1 18.7998 49.1 22.0998 48.7 22.7998C50.7 24.8998 51.9 27.6998 51.9 30.9998C51.9 42.7998 44.6 45.4998 37.8 46.1998C38.9 47.1998 39.9 49.1998 39.9 51.9998C39.9 56.1998 39.8 59.4998 39.8 60.4998C39.8 61.2998 40.4 62.1998 41.9 61.8998C54.1 57.7998 63 46.2998 63 32.5998C62.9 15.5998 49 1.7998 32 1.7998Z" />
                            </svg>
                        </a>
                        <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.maps"
                            class="hover:text-fuchsia-200">
                            <svg class=" fill-current" width="24" height="24" viewBox="0 0 64 64">
                                <path
                                    d="M10.2732 1L37.5939 28.3156L44.6439 21.2656C35.0104 15.4207 22.1078 7.57985 16.3051 4.05449L12.4175 1.69934C11.7304 1.28073 10.9946 1.05529 10.2732 1ZM6.10284 4.27047C6.04756 4.57061 6 4.87223 6 5.19607V59.1793C6 59.4057 6.04554 59.6165 6.07713 59.8324L33.871 32.0386L6.10284 4.27047ZM49.2771 24.0784L41.3169 32.0386L49.1383 39.8599C53.2823 37.3482 56.1525 35.6041 56.4711 35.4119C57.8797 34.5509 58.6751 33.252 58.6514 31.8329C58.6304 30.4401 57.8347 29.1949 56.4814 28.4287C56.1786 28.2549 53.3475 26.5453 49.2771 24.0784ZM37.5939 35.7616L10.3555 63C10.8847 62.9079 11.4132 62.75 11.9187 62.4446C12.6191 62.0181 31.5384 50.5396 44.5051 42.6727L37.5939 35.7616Z" />
                            </svg>
                        </a>
                        <a href="https://discord.gg/GEbN7DGb" class="hover:text-fuchsia-200">
                            <svg class=" fill-current" width="24" height="24" viewBox="0 0 64 64">
                                <path
                                    d="M26.3969 27.0996C24.5969 27.0996 23.2969 28.6996 23.2969 30.4996C23.2969 32.2996 24.6969 33.8996 26.3969 33.8996C28.1969 33.8996 29.4969 32.3996 29.4969 30.4996C29.5969 28.5996 28.1969 27.0996 26.3969 27.0996Z" />
                                <path
                                    d="M37.6 33.8C39.3121 33.8 40.7 32.2778 40.7 30.4C40.7 28.5222 39.3121 27 37.6 27C35.8879 27 34.5 28.5222 34.5 30.4C34.5 32.2778 35.8879 33.8 37.6 33.8Z" />
                                <path
                                    d="M52.6984 1H11.2984C7.79844 1 4.89844 3.8 4.89844 7.3V49.2C4.89844 52.7 7.69844 55.5 11.1984 55.5H46.2984L44.5984 49.9L48.4984 53.6L52.2984 57.1L58.8984 63V7.3C59.1984 3.8 56.1984 1 52.6984 1ZM40.6984 41.4C40.6984 41.4 39.5984 40.1 38.5984 38.9C42.6984 37.8 44.1984 35.2 44.1984 35.2C42.8984 36 41.6984 36.6 40.6984 37C39.1984 37.7 37.5984 38.1 36.1984 38.3C33.1984 38.9 30.5984 38.7 28.1984 38.3C26.3984 38 24.9984 37.5 23.6984 37C22.9984 36.7 22.0984 36.4 21.3984 36C21.2984 36 21.2984 35.9 21.0984 35.9C21.0984 35.9 20.9984 35.9 20.9984 35.8C20.3984 35.5 20.1984 35.2 20.1984 35.2C20.1984 35.2 21.7984 37.7 25.6984 38.9C24.6984 40 23.5984 41.4 23.5984 41.4C16.6984 41.1 14.1984 36.8 14.1984 36.8C14.1984 26.8 18.6984 18.8 18.6984 18.8C23.1984 15.4 27.3984 15.6 27.3984 15.6L27.6984 16C21.9984 17.5 19.4984 20 19.4984 20C19.4984 20 20.1984 19.6 21.2984 19.2C24.6984 17.8 27.1984 17.4 28.2984 17.2C28.3984 17.2 28.5984 17.2 28.8984 17.2C30.6984 16.9 32.9984 16.9 35.0984 17.2C38.0984 17.5 41.1984 18.5 44.3984 20.2C44.3984 20.2 41.9984 17.9 36.5984 16.3L36.9984 15.7C36.9984 15.7 41.1984 15.6 45.6984 18.9C45.6984 18.9 50.1984 26.9 50.1984 36.9C50.2984 36.8 47.5984 41.3 40.6984 41.4Z" />
                            </svg>
                        </a>
                    </div>
                </div>
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