#include "cpu_test.hpp"

#include <chrono>
#include <cmath>

CpuTestResult run_cpu_test(uint64_t iterations) {
    using clock = std::chrono::steady_clock;

    volatile double value = 1.0;

    auto start = clock::now();

    for (uint64_t i = 0; i < iterations; ++i) {
        value = std::sin(value) * 1.000001 + std::cos(value);
        value = value * 1.000001 + 0.000001;
    }

    auto end = clock::now();

    std::chrono::duration<double> elapsed = end - start;

    // Approximate number of floating-point operations performed
    // per loop iteration.
    constexpr double operations_per_iteration = 6.0;

    double operations =
        static_cast<double>(iterations) * operations_per_iteration;

    CpuTestResult result{};
    result.duration_seconds = elapsed.count();
    result.iterations = iterations;
    result.operations_per_second =
        operations / result.duration_seconds;
    result.checksum = value;

    return result;
}