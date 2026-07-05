def longestSubarrayWithSumK(a: [int], k: int) -> int:
    prefix_sum = 0
    max_length = 0
    prefix_map = {}

    for i in range(len(a)):
        prefix_sum += a[i]

        if prefix_sum == k:
            max_length = i + 1

        remaining = prefix_sum - k

        if remaining in prefix_map:
            length = i - prefix_map[remaining]
            if length > max_length:
                max_length = length

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length