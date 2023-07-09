<template>
    <div class="w-full max-h-screen grow flex bg-gray-200 lg:p-4 z-1">
        <div class="shell-container bg-white relative shadow-md rounded-lg container p-0 shrink-0">
            <aside class="menu rounded-l-lg flex flex-col justify-between gap-y-12 p-8 border-r border-neutral-100">
                <div class="logo-container p-2 flex items-center justify-center">
                    <img class="m-0 h-10 w-auto" src="/logos/lazy-lab-logo-25.svg" alt="Lazy Lab" />
                </div>
                <ul class="menu-links px-2 flex flex-col grow items-stretch gap-y-6 text-sm">
                    <div
                        class="p-3 px-5 shadow cursor-pointer text-neutral-50 shadow bg-neutral-900 font-medium rounded-md flex items-center justify-start gap-x-3">
                        <HomeIcon class="h-5 w-5" aria-hidden="true" />Overview
                    </div>
                    <div
                        class="p-3 px-5 cursor-pointer text-neutral-600 bg-neutral-100 hover:shadow rounded-md flex items-center justify-start gap-x-3">
                        <QrCodeIcon class="h-5 w-5" aria-hidden="true" />Tokens
                    </div>
                    <div
                        class="p-3 px-5 cursor-pointer text-neutral-600 bg-neutral-100 hover:shadow rounded-md flex items-center justify-start gap-x-3">
                        <BriefcaseIcon class="h-5 w-5" aria-hidden="true" />Clients
                    </div>
                    <div
                        class="p-3 px-5 cursor-pointer text-neutral-600 bg-neutral-100 hover:shadow rounded-md flex items-center justify-start gap-x-3">
                        <ServerStackIcon class="h-5 w-5" aria-hidden="true" />Equipment
                    </div>
                    <div
                        class="p-3 px-5 relative cursor-pointer text-neutral-600 bg-neutral-100 hover:shadow rounded-md flex items-center justify-start gap-x-3">
                        <WrenchScrewdriverIcon class="h-5 w-5" aria-hidden="true" />Repairs
                        <div
                            className="absolute -top-0.5 -right-1 w-5 h-5 grid place-items-center text-xs text-neutral-50 rounded-full bg-fuchsia-400">
                            3</div>
                    </div>
                    <div
                        class="p-3 px-5 relative cursor-pointer text-neutral-600 bg-neutral-100 hover:shadow rounded-md flex items-center justify-start gap-x-3">
                        <ChatBubbleLeftRightIcon class="h-5 w-5" aria-hidden="true" />
                        Conversations
                        <div
                            className="absolute -top-0.5 -right-1 w-5 h-5 grid place-items-center text-xs text-neutral-50 rounded-full bg-amber-400">
                            12</div>
                    </div>

                </ul>
                <div class="avatar-holder flex flex-col items-center gap-y-3">
                    <div className="relative w-14 h-14">
                        <span
                            className="absolute -bottom-px right-1 w-3 h-3 rounded-full border border-white bg-green-500"></span>
                        <img src="https://images.unsplash.com/photo-1510227272981-87123e259b17?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=3759e09a5b9fbe53088b23c615b6312e"
                            className="w-full h-full rounded-full" />
                    </div>
                    <div class="flex flex-col items-center">
                        <span class="text-neutral-700 font-semibold text-sm">{{ auth.user?.name }}</span>
                        <span class="user-email text-neutral-400 text-xs">{{ auth.user?.email }}</span>
                    </div>
                    <div class="flex gap-x-4">
                        <button
                            className="px-2.5 py-2.5 text-neutral-600 duration-150 bg-neutral-100 rounded-lg hover:bg-fuchsia-100 active:bg-fuchsia-200">
                            <Cog8ToothIcon class="h-6 w-6" aria-hidden="true" />
                        </button>
                        <button
                            className="px-2.5 py-2.5 text-neutral-600 duration-150 bg-neutral-100 rounded-lg hover:bg-fuchsia-100 active:bg-fuchsia-200">
                            <PowerIcon class="h-6 w-6" aria-hidden="true" />
                        </button>
                    </div>
                </div>
            </aside>
            <header
                class="content-header rounded-tr-lg bg-white p-8 flex flex-row justify-between items-center flex-nowrap">
                <div class="w-1/2">
                    <h2 class="text-3xl font-semibold">Overview</h2>
                    <span class="text-sm text-neutral-400">Quick preview for all activities.</span>

                </div>
                <div class="w-1/2 flex items-center justify-end gap-x-4">
                    <form class="max-w-sm">
                        <div class="relative">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="absolute top-0 bottom-0 w-6 h-6 my-auto text-gray-600 left-3" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            <input type="text" placeholder="Search"
                            class="w-full py-2 pl-12 pr-4 text-neutral-800 border rounded-md outline-none bg-gray-50 focus:bg-white focus:border-fuchsia-400" />
                        </div>
                    </form>
                    <button
                        className="relative px-2.5 py-2.5 text-neutral-600 duration-150 bg-neutral-100 rounded-lg hover:bg-fuchsia-50" @click="test++">
                        <BellIcon class="h-6 w-6" aria-hidden="true" />
                        <Notifier :count="test"> </Notifier>
                    </button>
                </div>
            </header>
            <main class="main-content bg-white rounded-br-lg flex items-center justify-center overflow-y-hidden">
                <Bubbles :count=6 :opacity=0.66 :speed=0.66 :scale="0.66">   
                    <div class="relative p-8 py-6 rounded-lg shadow-inner bg-neutral-50 text-neutral-400 z-20">
                        There are no items yet, go ahead and add something!
                    </div>
                </Bubbles>

            </main>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

import { HomeIcon, BriefcaseIcon, ServerStackIcon, WrenchScrewdriverIcon, ChatBubbleLeftRightIcon, QrCodeIcon, Cog8ToothIcon, PowerIcon, BellIcon } from '@heroicons/vue/24/outline';
import { Bubbles } from '../../components/Bubbles';
import { Notifier } from '../../components/Notifier';

import { useAuth } from '@/stores/auth';

const test = ref(0);

const auth = useAuth();

</script>

<style lang="scss" scoped>
.shell-container {
    display: grid;
    grid-template-columns: 4fr 6fr 15fr;
    grid-template-rows: minmax(120px, 2fr) 14fr 2fr;
    grid-column-gap: 2rem;
    grid-row-gap: 0;
    max-height: 100%;
}

.search-bar {
    grid-area: 1 / 2 / 2 / 3;
}

.content-header {
    grid-area: 1 / 2 / 2 / 4;
    font-family: Poppins;
}

.main-content {
    grid-area: 2 / 2 / 4 / 4;
}

.menu {
    grid-area: 1 / 1 / 4 / 2;

    .user-email {
        font-family: Poppins;
    }
}
</style>