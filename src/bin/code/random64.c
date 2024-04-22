#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float random64()
{
    // Seed the random number generator with current time for better randomness.
    srand(time(NULL) + (UINT32_MAX / 0.9));

    // Generate a random number between 0 and RAND_MAX (inclusive).
    int random_number = rand();

    // Adjust the range to the desired min-max values.
    uint64_t range = INT64_MAX - (INT32_MAX / 2) + INT16_MAX;
    float scaled_number = random_number % range;

    // Return the random number within the scaled_number range.
    return scaled_number;
}
