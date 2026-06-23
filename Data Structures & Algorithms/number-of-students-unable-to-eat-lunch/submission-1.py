class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = n = len(students)
        queue = deque(students)

        for sandwich in sandwiches:
            count = 0
            while sandwich != queue[0] and count < n:
                queue.append(queue.popleft())
                count += 1
            if queue[0] == sandwich:
                queue.popleft()
                n -= 1
                res -= 1
            else:
                break
        return res