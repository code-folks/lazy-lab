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

const MIN_DELAY = 100;
const MIN_DURATION = 1.5;

export function useBubbles(count: number, zIndex: number): UseBubbles {
    const bubbles = new Set<Bubble>();
    for (let i = 0; i < count; i++) {
        let size = randomFloat(1, 4);
        let offset = randomInt(5, 50);
        let side = i%2 == 0 ? 'right': 'left';
        let kind = 1 + i%4;
        bubbles.add(
            {
                blockStyle: {
                    animation: `up ${randomFloat(MIN_DURATION, 6)}s ${randomInt(MIN_DELAY, 400)}ms infinite`,
                    width: `${size}rem`,
                    height: `${size}rem`,
                    top: '1rem',
                    [side]: `${offset}%`,
                    overflowY: 'visible',
                    zIndex: zIndex,
                    position: 'absolute'
                },
                src: `/img/bubble-${kind}.svg`,
                style: {
                    animation: `wobble ${randomFloat(MIN_DURATION, 5)}s ${randomInt(MIN_DELAY, 430)}ms infinite`,
                    zIndex: zIndex + 1,
                    position: 'relative',
                    width: '100%',
                    height: '100%'
                },
            }
        )
    }
    return {
        bubbles
    }
}