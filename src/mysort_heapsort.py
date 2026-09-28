"""힙 정렬 예제."""


def heap_sort(values):
	"""values를 제자리에서 오름차순으로 정렬하고 반환한다."""
	def sift_down(root, end):
		while 2 * root + 1 < end:
			child = 2 * root + 1
			if child + 1 < end and values[child] < values[child + 1]:
				child += 1
			if values[root] >= values[child]:
				return
			values[root], values[child] = values[child], values[root]
			root = child

	size = len(values)
	for root in range(size // 2 - 1, -1, -1):
		sift_down(root, size)

	for end in range(size - 1, 0, -1):
		values[0], values[end] = values[end], values[0]
		sift_down(0, end)

	return values


if __name__ == "__main__":
	data = [37, 12, 25, 37, 8, 19, 4, 25, 31, 16, 8, 42, 3, 19, 27]
	print(heap_sort(data))
