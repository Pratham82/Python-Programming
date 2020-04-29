import sys

def read_series(filename):
    try:
        with open(filename,mode='rt',encoding='utf-8') as f:
            f.write(f"{r}\n" for r in islice(sequence(), num+1))
    finally:
        f.close()

def main(filename):
    series = read_series(filename)
    print(series)