
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        answer = []

        while len(answer) < k:
            biggest_num = None
            biggest_count = 0

            for num in counts:
                if counts[num] > biggest_count:
                    biggest_num = num
                    biggest_count = counts[num]

            answer.append(biggest_num)
            del counts[biggest_num]

        return answer