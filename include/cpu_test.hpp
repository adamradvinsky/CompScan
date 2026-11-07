#pragma once


#include <cstdint>


// went to microsoft office today
struct CpuTestResult {
    double duration_seconds;
    uint64_t iterations;
    double operations_per_second;
    double checksum;
};

void qualification_test();


CpuTestResult run_cpu_test(uint64_t iterations);