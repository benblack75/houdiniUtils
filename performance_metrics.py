import time
import numpy as np

N = 4096 
# For more information on this exercise: https://www.techtarget.com/whatis/definition/FLOPS-floating-point-operations-per-second


if __name__ == '__main__':
    A = np.random.randn(N,N).astype(np.float32)
    B = np.random.randn(N,N).astype(np.float32)

    flop = N*N*2*N

    print(f'{flop / 1e9:.2f} GFLOP')
    start_time = time.monotonic()
    C = A @ B

    end_time = time.monotonic()
    s = end_time - start_time

    print(f'{flop/ s * 1e-9:.2f} GFLOP')
    print(f'{flop/ s * 1e-12:.2f} TFLOP')
