
function sample<T>(arr : T[]): T | undefined {
    const len = arr == null ? 0 : arr.length
    return len ? arr[Math.floor(Math.random() * len)] : undefined
}

function randomFloat(min: number, max: number, precision: number = 2): number {
    const rangeWidth = max - min;
    return +( min + (Math.random() * rangeWidth)).toFixed(precision);
}

function randomInt(min: number, max: number): number {
    const rangeWidth = max - min;
    return Math.round(min + (Math.random() * rangeWidth));
}

export {
    sample,
    randomFloat,
    randomInt
}
