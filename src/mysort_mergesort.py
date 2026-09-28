"""병합 정렬 예제."""


def merge_sort(values):
	"""values를 제자리에서 오름차순으로 정렬하고 반환한다."""
	buffer = values.copy()

	def sort_range(start, end):
		if end - start < 2:
			return

		middle = (start + end) // 2
		sort_range(start, middle)
		sort_range(middle, end)

		left = start
		right = middle
		for index in range(start, end):
			if left < middle and (right >= end or values[left] <= values[right]):
				buffer[index] = values[left]
				left += 1
			else:
				buffer[index] = values[right]
				right += 1
		values[start:end] = buffer[start:end]

	sort_range(0, len(values))
	return values


if __name__ == "__main__":
	data = [37, 12, 25, 37, 8, 19, 4, 25, 31, 16, 8, 42, 3, 19, 27]
	print(merge_sort(data))
