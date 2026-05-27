/**
 * Metering Utils Stub
 * Smriti doesn't use metering/billing, but keeping this for compatibility
 */

export const toMicroCents = (dollars: number): number => {
    // Convert dollars to microcents (1 dollar = 1,000,000 microcents)
    // For Smriti, this is just a stub since we don't do billing
    return Math.round(dollars * 1000000);
};

// Stub for any other metering utilities that might be needed
export const fromMicroCents = (microcents: number): number => {
    return microcents / 1000000;
};
