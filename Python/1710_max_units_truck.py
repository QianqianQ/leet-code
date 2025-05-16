class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_boxes = 0
        boxTypes.sort(key=lambda x: -x[1])

        for no_of_boxtype, no_of_units in boxTypes:
            if truckSize >= no_of_boxtype:
                total_boxes += no_of_boxtype * no_of_units
                truckSize -= no_of_boxtype
            elif truckSize > 0:
                total_boxes += truckSize * no_of_units
                return total_boxes

        return total_boxes


if __name__ == '__main__':
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    print(Solution().maximumUnits(boxTypes, truckSize))  # Output: 8