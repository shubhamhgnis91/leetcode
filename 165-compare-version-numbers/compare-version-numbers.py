class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]

        diff = len(v1) - len(v2)
        v1 += [0] * -diff
        v2 += [0] * diff

        return (v1 > v2) - (v1 < v2)