import cProfile
import gc
import json
import time
import tracemalloc

import pytest
from pytest_benchmark.plugin import benchmark

from sl_optimizer.layout import StorageLayout
from tests.conftest import get_fixture_path

gc.disable()


@pytest.fixture
def layout():
    filepath = get_fixture_path("super_nested_structure_storage.json")
    with open(filepath) as f:
        layout = json.load(f)

    return layout


@pytest.fixture
def sl(layout):
    return StorageLayout(data=layout)


@pytest.mark.benchmark(disable_gc=True, warmup=True)
def test_run_benchmark(sl, benchmark):
    benchmark.pedantic(sl.optimize, iterations=10, rounds=100)


def test_cprofile(sl):
    with cProfile.Profile() as pr:
        tracemalloc.start()
        sl.optimize()
        print(
            f"The current size and peak size of memory blocks traced by tracemalloc: {tracemalloc.get_traced_memory()}"
        )
        tracemalloc.stop()

    pr.print_stats()


def test_timeit(sl):
    start_time = time.perf_counter()
    sl.optimize()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")


def main():
    ...


if __name__ == "__main__":
    # do not launch this from IDE environment
    main()
