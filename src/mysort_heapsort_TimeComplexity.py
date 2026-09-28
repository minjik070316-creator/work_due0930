import ast
from pathlib import Path
from time import perf_counter_ns


def heap_sort(values):
	"""values를 제자리에서 오름차순으로 정렬한다."""
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


def main():
	original = ast.literal_eval(Path(__file__).with_name("10000random_integer_data").read_text())

	run_times_ms = []
	sorted_results = []
	for run in range(1, 6):
		values = original.copy()
		start = perf_counter_ns()
		heap_sort(values)
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
