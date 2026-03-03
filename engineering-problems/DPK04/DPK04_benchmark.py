import timeit
import sys

from DPK04_large_pairs import get_language as get_language_string
from DPK04_large_tuples import get_language as get_language_tuple


def benchmark_versions():
    # Random order
    # test_countries = ["Usa", "Japan", "Brazil", "Germany", "Australia", "PapuaNewGuinea"]
    
    #first_countries
    # test_countries = ["Usa", "Brazil", "Spain", "Italy", "France", "Germany"]
    
    #last_countries
    test_countries = ["PapuaNewGuinea","EastTimor","Brunei","Macau","HongKong","Taiwan",]
    
    print("=" * 70)
    print("BENCHMARK: String Format vs Tuple Format")
    print("=" * 70)
    print()
    
    total_string_time = 0
    total_tuple_time = 0
    
    for country in test_countries:

        string_time = timeit.timeit(
            f'get_language_string("{country}")',
            setup='from DPK04_large_pairs import get_language as get_language_string',
            number=100000
        )

        tuple_time = timeit.timeit(
            f'get_language_tuple("{country}")',
            setup='from DPK04_large_tuples import get_language as get_language_tuple',
            number=100000
        )
        
        total_tuple_time += tuple_time
        total_string_time += string_time

        speedup = string_time / tuple_time
        print(f"{country:15} | String: {string_time:.4f}s | Tuple: {tuple_time:.4f}s | Speedup: {speedup:.2f}x")
    
    print()
    print("=" * 70)
    print(f"TOTAL          | String: {total_string_time:.4f}s | Tuple: {total_tuple_time:.4f}s | Speedup: {total_string_time/total_tuple_time:.2f}x")
    print("=" * 70)
    
    # Memory usage
    from DPK04_large_pairs import data as string_data
    from DPK04_large_tuples import data as tuple_data
    
    print()
    print("Memory Usage:")
    print(f"String data: {sys.getsizeof(string_data)} bytes")
    print(f"Tuple data:  {sys.getsizeof(tuple_data)} bytes")


if __name__ == "__main__":
    benchmark_versions()
