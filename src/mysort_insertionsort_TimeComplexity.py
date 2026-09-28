import ast
from pathlib import Path
from time import perf_counter_ns


def insertion_sort(values):
	"""values를 제자리에서 오름차순으로 정렬한다."""
	for index in range(1, len(values)):
		value = values[index]
		position = index - 1
		while position >= 0 and values[position] > value:
			values[position + 1] = values[position]
			position -= 1
		values[position + 1] = value
	return values


def main():
	original = ast.literal_eval(Path(__file__).with_name("10000random_integer_data").read_text())

	run_times_ms = []
	sorted_results = []
	for run in range(1, 6):
		values = original.copy()
		start = perf_counter_ns()
		insertion_sort(values)
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
