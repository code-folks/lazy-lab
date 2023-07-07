import { randomFloat, randomInt } from "../utils/random";
import { StyleValue } from "vue";

interface Bubble {
    blockStyle: StyleValue,
    src: string,
    style: StyleValue
}

interface UseBubbles {
    bubbles: Set<Bubble>
}

const MIN_DELAY = 80;
const MIN_DURATION = 4.2;
const BASE_DELAY = 60;
const DURATION_BASE = 1;
const WOOBLE_FACTOR = 0.8;

export function useBubbles(count: number, zIndex: number, speed: number = 1, opacity: number = 1, scale: number = 1): UseBubbles {
    const bubbles = new Set<Bubble>();
    const durationMultipler = DURATION_BASE / (speed || 1);
    for (let i = 0; i < count; i++) {
        let size = randomFloat(1, 4) * scale;
        let offset = randomInt(2 + size, 48);
        let side = i % 2 == 0 ? 'right' : 'left';
        let kind = 1 + i % 5;
        let maxDelay = ((2 * MIN_DELAY) + (BASE_DELAY * i) * durationMultipler)
        bubbles.add(
            {
                blockStyle: {
                    animation: `up ${randomFloat(MIN_DURATION, 6.8) * durationMultipler}s ${randomInt(MIN_DELAY, maxDelay)}ms infinite`,
                    width: `${size}rem`,
                    height: `${size}rem`,
                    top: `${size}rem`,
                    [side]: `${offset}%`,
                    overflowY: 'visible',
                    zIndex: zIndex,
                    position: 'absolute',
                    opacity: 0,
                    visibility: 'hidden'
                },
                src: `/img/bubble-${kind}.svg`,
                style: {
                    animation: `wobble ${randomFloat(1.5, 5) * durationMultipler}s ${randomInt(MIN_DELAY, maxDelay * WOOBLE_FACTOR)}ms infinite`,
                    zIndex: zIndex + 1,
                    position: 'relative',
                    width: '100%',
                    height: '100%',
                    opacity: opacity
                },
            }
        )
    }
    return {
        bubbles
    }
}