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
	original = [
		42, 128, 753, 512, 890, 14, 637, 209, 945, 381,
		42, 618, 274, 803, 128, 956, 421, 67, 539, 712,
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
		heap_sort(values)
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
