/**
 * Metering Constants Stub
 * Smriti doesn't use metering/billing, but keeping this for compatibility
 */

// Stub constants for metering
export const METERING_ENABLED = false;

// Cost constants (all set to 0 for Smriti since it's free and local)
export const DEFAULT_COSTS = {
    'ai:chat:tokens': 0,
    'ai:image:generation': 0,
    'ai:speech:synthesis': 0,
    'ai:speech:recognition': 0,
    'filesystem:storage:bytes': 0,
    'filesystem:ingress:bytes': 0,
    'filesystem:egress:bytes': 0,
} as const;

// Stub for any other metering constants
export const MICROCENTS_PER_DOLLAR = 1000000;
