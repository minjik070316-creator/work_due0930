"""삽입 정렬 예제."""


def insertion_sort(values):
	"""values를 제자리에서 오름차순으로 정렬하고 반환한다."""
	for index in range(1, len(values)):
		value = values[index]
		position = index - 1
		while position >= 0 and values[position] > value:
			values[position + 1] = values[position]
			position -= 1
		values[position + 1] = value
	return values


if __name__ == "__main__":
	data = [37, 12, 25, 37, 8, 19, 4, 25, 31, 16, 8, 42, 3, 19, 27]
	print(insertion_sort(data))
