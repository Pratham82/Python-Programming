if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	set1 = sorted(list(set(arr)))
	print(set1[-2])
	