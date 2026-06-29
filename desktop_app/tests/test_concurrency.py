"""
Tests for AIMDConcurrencyController limits, thresholds, throttling, and recovery behaviors.
"""

import pytest
from workers.scan_queue import AIMDConcurrencyController


def test_concurrency_initialization_bounds():
    # Ceiling cap initial value
    controller = AIMDConcurrencyController(floor=2, ceiling=5)
    assert 2 <= controller.current_limit() <= 5

    # Start value under floor maps to floor
    controller2 = AIMDConcurrencyController(floor=4, ceiling=8)
    assert controller2.current_limit() >= 4


def test_aimd_multiplicative_decrease():
    # Beta = 0.5 (halve concurrency)
    controller = AIMDConcurrencyController(floor=1, ceiling=16)
    
    # Manually increase concurrency
    controller.concurrency = 12
    assert controller.current_limit() == 12

    # First throttle event
    controller.on_throttle(retry_after_s=1.5)
    assert controller.current_limit() == 6

    # Second throttle event
    controller.on_throttle(retry_after_s=0.0)
    assert controller.current_limit() == 3

    # Third throttle event
    controller.on_throttle(retry_after_s=0.0)
    assert controller.current_limit() == 1  # 3 * 0.5 = 1.5 -> floor to 1

    # Fourth throttle event remains at floor of 1
    controller.on_throttle(retry_after_s=0.0)
    assert controller.current_limit() == 1


def test_aimd_additive_increase():
    # Ceiling = 4
    controller = AIMDConcurrencyController(floor=1, ceiling=4, additive_step=1)
    controller.concurrency = 1
    assert controller.current_limit() == 1

    # Ramping up concurrency requires successful ticks
    # Each success adds: 1 / current_concurrency
    # At concurrency = 1, it takes 1 success to reach 2
    controller.on_success(100.0)
    assert controller.current_limit() == 2

    # At concurrency = 2, it takes 2 successes to reach 3
    controller.on_success(100.0)
    assert controller.current_limit() == 2
    controller.on_success(100.0)
    assert controller.current_limit() == 3

    # At concurrency = 3, it takes 3 successes to reach 4
    controller.on_success(100.0)
    assert controller.current_limit() == 3
    controller.on_success(100.0)
    assert controller.current_limit() == 3
    controller.on_success(100.0)
    assert controller.current_limit() == 4

    # Remains capped at ceiling of 4
    for _ in range(10):
        controller.on_success(50.0)
    assert controller.current_limit() == 4


def test_aimd_error_decrease():
    controller = AIMDConcurrencyController(floor=2, ceiling=8)
    controller.concurrency = 6
    assert controller.current_limit() == 6

    # Error reduces limit by 1 (subtractive penalty)
    controller.on_error()
    assert controller.current_limit() == 5

    controller.on_error()
    assert controller.current_limit() == 4

    # Keep erroring down to floor
    for _ in range(10):
        controller.on_error()
    assert controller.current_limit() == 2


def test_aimd_dynamic_fractional_accumulation():
    controller = AIMDConcurrencyController(floor=1, ceiling=8, additive_step=2)
    controller.concurrency = 4
    
    # Step = 2, concurrency = 4. Each success adds 2/4 = 0.5
    controller.on_success(100.0)
    assert controller.current_limit() == 4  # fraction accumulated = 0.5
    
    controller.on_success(100.0)
    assert controller.current_limit() == 5  # fraction reaches 1.0, concurrency jumps by 1 (which is 2 * 0.5) to 5
