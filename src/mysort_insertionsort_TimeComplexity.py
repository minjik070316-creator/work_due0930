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
	original = [
		305, 849, 162, 753, 694, 88, 923, 451, 128, 576,
		234, 681, 915, 348, 702, 159, 826, 493, 75, 614,
		938, 267, 580, 143, 872, 329, 650, 901, 416, 82,
		735, 298, 561, 184, 827, 370, 643, 917, 482, 59,
		764, 215, 532, 198, 865, 341, 679, 904, 438, 91,
		720, 253, 589, 167, 814, 395, 628, 971, 402, 36,
		783, 226, 519, 173, 857, 304, 692, 936, 475, 21,
		749, 282, 540, 111, 838, 363, 607, 982, 469, 54,
	]

	print("정렬 전 원본 배열:")
	print(original)

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

	print("정렬 후 결과 배열:")
	print(sorted_results[-1])

	expected = sorted(original)
	passed = all(result == expected for result in sorted_results)
	print(f"오름차순 정렬 검증: {'PASS' if passed else 'FAIL'}")
	print(f"5회 실행시간 평균: {sum(run_times_ms) / len(run_times_ms):.6f} ms")


if __name__ == "__main__":
	main()
