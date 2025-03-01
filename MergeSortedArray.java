You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (nums2.length == 0) {
            return;
        }
        ArrayList<Integer> integers = new ArrayList<>();
        int i = 0, j = 0;
        while (i < m) {
            if (j < n) {
                if (nums1[i] <= nums2[j]) {
                    integers.add(nums1[i]);
                    i++;
                } else {
                    integers.add(nums2[j]);
                    j++;
                }
            } else {
                integers.add(nums1[i]);
                i++;
            }
        }
        for (int k = j; k < n; k++) {
            integers.add(nums2[k]);
        }
        for (int k = 0; k < nums1.length; k++) {
            nums1[k] = integers.get(k);
        }
    }
}