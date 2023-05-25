<template>
    <div class="w-full grow flex items-center lg:py-8">
        <div class="shell-container bg-shell relative lg:rounded-lg container p-0 grow">
            <div class="menu shadow-md bg-neutral-900 lg:rounded-l-lg"></div>
            <div class="search-bar border-r border-b border-zinc-100"> </div>
            <aside class="side-content border-r border-zinc-100"></aside>
            
            <header
                class="container content-header p-3 max-w-screen-xl flex flex-row justify-between items-center flex-nowrap border-b border-zinc-100">
                <div class="w-1/3"></div>
                <Profile class=""></Profile>
            </header>
            <main class="main-content flex flex-row items-center justify-center">
                
            </main>
        </div>
    </div>
</template>

<script lang="ts" setup>
import Profile from '../../components/Profile.vue';


</script>

<style lang="scss" scoped>
.shell-container {
    display: grid;
    grid-template-columns: 1fr 5fr 15fr;
    grid-template-rows: 1fr 10fr 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    height: max(720px, 86%);
    max-height: 100%;
}

.search-bar {
    grid-area: 1 / 2 / 2 / 3;
}

.content-header {
    grid-area: 1 / 3 / 2 / 4;
}

.main-content {
    grid-area: 2 / 3 / 4 / 4;
}

.side-content {
    grid-area: 2 / 2 / 4 / 3;
}

.menu {
    grid-area: 1 / 1 / 4 / 2;
}
</style>