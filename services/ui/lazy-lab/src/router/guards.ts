import { NavigationGuardWithThis, RouteLocationNormalized } from "vue-router";
import { useTitle } from '@vueuse/core'

import { sample } from "../utils/random";

const RANDOM_TITLES: string[] = [
    "Time for a coffee break",
    "Have a nice day",
    "You can do this tomorrow",
    "Sometimes I get lost",
    "It's a piece of cake",
    "Don't overdo it!",
    "I hope your day is as beautiful as your smile",
    "Don't worry, it's one day closer to the weekend",
]

const updateTitleGuard: NavigationGuardWithThis<undefined> = (to: RouteLocationNormalized) => {
    const randomTitle = sample(RANDOM_TITLES) || "Opps";
    const routeTitle: string = typeof to.meta.title === 'string' ? to.meta.title : randomTitle;
    useTitle(routeTitle, {titleTemplate: '%s | LazyLab'});
}

export {
    updateTitleGuard,
}