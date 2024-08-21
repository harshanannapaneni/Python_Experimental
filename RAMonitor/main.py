import psutil

memory = psutil.virtual_memory()

def ram_usage():
    # We divide by 10^9 as we want to fetch the results in gigabytes(10^9 bytes)
    print(f"Total avaiable memory in gigabytes "
          f"{memory.total/(1024**3):.3f}")
    print(f"Total used memory in gigabytes "
          f"{memory.used/(1024**3):.3f}")
    print(f"Percentage of memory under use:"
          f"{memory.percent}%")
    
ram_usage()
