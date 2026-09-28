"""삽입 정렬의 안정성을 확인한다."""

from mysort_insertionsort import insertion_sort


class ScoreItem:
	"""점수만 정렬 기준으로 사용하는 항목."""

	def __init__(self, score, label):
		self.score = score
		self.label = label

	def __gt__(self, other):
		return self.score > other.score


def format_items(items):
	return ", ".join(f"({item.score}, {item.label})" for item in items)


if __name__ == "__main__":
	data = [
		ScoreItem(80, "A"),
		ScoreItem(70, "B"),
		ScoreItem(80, "C"),
		ScoreItem(60, "D"),
		ScoreItem(80, "E"),
	]
	original_80_order = [item.label for item in data if item.score == 80]

	print(f"정렬 전 데이터: {format_items(data)}")
	insertion_sort(data)
	print(f"정렬 후 데이터: {format_items(data)}")

	sorted_80_order = [item.label for item in data if item.score == 80]
	print(f"동일한 점수인 80점 원소들의 정렬 전 순서: {', '.join(original_80_order)}")
	print(f"정렬 후 80점 원소들의 순서: {', '.join(sorted_80_order)}")
	print("Stable: PASS" if original_80_order == sorted_80_order else "Stable: FAIL")
