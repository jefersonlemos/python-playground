# BENCHMARK: String Format vs Tuple Format


# Random order
```
Usa             | String: 0.3679s | Tuple: 0.0176s | Speedup: 20.95x
Japan           | String: 0.4829s | Tuple: 0.0368s | Speedup: 13.11x
Brazil          | String: 0.3478s | Tuple: 0.0180s | Speedup: 19.31x
Germany         | String: 0.5260s | Tuple: 0.0237s | Speedup: 22.20x
Australia       | String: 0.6977s | Tuple: 0.0981s | Speedup: 7.11x
PapuaNewGuinea  | String: 1.9302s | Tuple: 0.3240s | Speedup: 5.96x

======================================================================
TOTAL          | String: 4.3525s | Tuple: 0.5182s | Speedup: 8.40x
======================================================================

Memory Usage:
String data: 1822 bytes
Tuple data:  936 bytes
```

# First countries
```
Usa             | String: 0.3413s | Tuple: 0.0097s | Speedup: 35.17x
Brazil          | String: 0.3832s | Tuple: 0.0153s | Speedup: 25.03x
Spain           | String: 0.4575s | Tuple: 0.0165s | Speedup: 27.80x
Italy           | String: 0.4649s | Tuple: 0.0170s | Speedup: 27.42x
France          | String: 0.3433s | Tuple: 0.0220s | Speedup: 15.58x
Germany         | String: 0.3596s | Tuple: 0.0248s | Speedup: 14.51x

======================================================================
TOTAL          | String: 2.3498s | Tuple: 0.1052s | Speedup: 22.33x
======================================================================

Memory Usage:
String data: 1822 bytes
Tuple data:  936 bytes
```

# Last countries
```
PapuaNewGuinea  | String: 2.0823s | Tuple: 0.3202s | Speedup: 6.50x
EastTimor       | String: 1.7918s | Tuple: 0.2967s | Speedup: 6.04x
Brunei          | String: 1.8036s | Tuple: 0.3428s | Speedup: 5.26x
Macau           | String: 1.9455s | Tuple: 0.3209s | Speedup: 6.06x
HongKong        | String: 1.7159s | Tuple: 0.3265s | Speedup: 5.25x
Taiwan          | String: 1.8453s | Tuple: 0.3072s | Speedup: 6.01x

======================================================================
TOTAL          | String: 11.1845s | Tuple: 1.9144s | Speedup: 5.84x
======================================================================

Memory Usage:
String data: 1822 bytes
Tuple data:  936 bytes
```
