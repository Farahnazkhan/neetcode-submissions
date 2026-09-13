class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let longestLen = 0;
        const numSet = new Set(nums);
        for (const num of nums) {
            // is this start of a sequence
            if (!numSet.has(num - 1)) {
                let length = 1;
                let sequence = num;
                while (numSet.has(sequence + 1)) {
                    length += 1;
                    sequence += 1;
                }
                longestLen = Math.max(longestLen, length);
            }
        }
        return longestLen
    }
}
