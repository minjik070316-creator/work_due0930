import ast
from pathlib import Path
from time import perf_counter_ns


def merge_sort(values):
	"""values를 제자리에서 오름차순으로 정렬한다."""
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


def main():
	original = ast.literal_eval(Path(__file__).with_name("10000random_integer_data").read_text())
	run_times_ms = []
	sorted_results = []
	for run in range(1, 6):
		values = original.copy()
		start = perf_counter_ns()
		merge_sort(values)
		elapsed_ms = (perf_counter_ns() - start) / 1_000_000
		run_times_ms.append(elapsed_ms)
		sorted_results.append(values)
		print(f"{run}회차 정렬 시간: {elapsed_ms:.6f} ms")

	expected = sorted(original)
	passed = all(result == expected for result in sorted_results)
	print(f"오름차순 정렬 검증: {'PASS' if passed else 'FAIL'}")
	print(f"5회 실행시간 평균: {sum(run_times_ms) / len(run_times_ms):.6f} ms")


if __name__ == "__main__":
	main()
