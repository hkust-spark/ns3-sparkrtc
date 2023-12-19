
#ifndef COMMON_HEADER_H
#define COMMON_HEADER_H


// Enable debug output
// #define ENABLE_DEBUG_OUTPUT

#ifdef ENABLE_DEBUG_OUTPUT
#define DEBUG(msg)                                    \
    do {                                              \
        std::cout << msg << std::endl;                \
    } while (false)
#else
#define DEBUG(msg)
#endif

#define MIN(x, y) ((x) <= (y) ? (x) : (y))
#define MAX(x, y) ((x) <= (y) ? (y) : (x))

#include <cinttypes>
#include <vector>
#include <string>

static inline bool Uint16Less (int a, int b) 
{
    if (a < b && a + UINT16_MAX / 2 > b)
        return true;
    else if (a > b && a > b + UINT16_MAX / 2)
        return true;
    else
        return false;
}

static inline bool Uint64Less (uint64_t id1, uint64_t id2) 
{
    uint64_t noWarpSubtract = id2 - id1;
    uint64_t wrapSubtract = id1 - id2;
    return noWarpSubtract < wrapSubtract;
}

#endif /* COMMON_HEADER_H */
