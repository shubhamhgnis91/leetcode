class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {0: students.count(0), 1: students.count(1)}
        k = 0

        while k < len(sandwiches) and count.get(sandwiches[k], 0) > 0:
            count[sandwiches[k]] -= 1
            k += 1

        return len(students) - k
