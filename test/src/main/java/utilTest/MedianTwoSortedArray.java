package utilTest;

public class MedianTwoSortedArray {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        //搜寻中位数，采取缩小范围的方法,通过start和length逼近
        //由特殊到一般，从做简单的情况发现解决办法，然后推广
        int length1 = nums1.length;
        int length2 = nums2.length;
        int start1 = 0;
        int start2 = 0;
        double median1;
        double median2;
        if (length1 == 0) {  //nums1为空
            if (length2 % 2 == 0) //有偶数个
                return (nums2[start2 + length2 / 2 - 1] + nums2[start2 + length2 / 2]) / 2.0;
            else {
                return nums2[start2 + length2 / 2];
            }
        }
        if (length2 == 0) {  //nums2为空
            if (length1 % 2 == 0) //有偶数个
                return (nums1[start1 + length1 / 2 - 1] + nums1[start1 + length1 / 2]) / 2.0;
            else {
                return nums1[start1 + length1 / 2];
            }
        }
        while (length1 > 0 && length2 > 0) {
            if (length1 == 1) {  //nums1只有一个元素
                if (length2 == 1) {
                    return (nums1[start1] + nums2[start2]) / 2.0;  //这个逻辑有问题。
                } else {
                    return getMedian(nums2, start2, length2, nums1[start1]);
                }
            }
            if (length2 == 1) {
                return getMedian(nums1, start1, length1, nums2[start2]);
            }
            if (length1 % 2 == 0 && length2 % 2 == 0) { //两个子数组长度都为偶数
                int nums1_m1 = nums1[start1 + length1 / 2 - 1];
                int nums1_m2 = nums1[start1 + length1 / 2];
                int nums2_m1 = nums2[start2 + length2 / 2 - 1];
                int nums2_m2 = nums2[start2 + length2 / 2];
                if (nums1_m1 >= nums2_m1) {
                    if (nums1_m2 <= nums2_m2) {
                        return (nums1_m1 + nums1_m2) / 2;
                    } else {
                        length1--;
                        length2--;
                        start2++;
                    }
                } else {
                    if (nums1_m2 >= nums2_m2) {
                        return (nums2_m1 + nums2_m2) / 2;
                    } else {
                        length1--;
                        length2--;
                        start2++;
                    }

                }
            }
            if (length1 % 2 == 1 && length2 % 2 == 1) { //长度都为奇数
                int nums1_m = nums1[start1 + length1 / 2];
                int nums2_m = nums2[start2 + length2 / 2];
                if (nums1_m == nums2_m) {
                    return nums1_m;
                }
                if (nums1_m > nums2_m) {
                    length1 = length1 / 2 + 1;
                    length2 = length2 / 2;
                    start2 = start2 + length2 + 1;
                } else {
                    length1 = length1 / 2;
                    length2 = length2 / 2 + 1;
                    start1 = start1 + length1 + 1;
                }
            } else {
                if (length1 % 2 == 1) { //nums1长度为奇数，nums2长度为偶数
                    int nums1_m = nums1[start1 + length1 / 2];
                    int nums2_m1 = nums2[start2 + length2 / 2 - 1];
                    int nums2_m2 = nums2[start2 + length2 / 2];
                    if (nums1_m >= nums2_m1) {
                        if (nums1_m <= nums2_m2) {
                            return nums1_m;
                        } else {
                            length1 = length1 / 2 + 1;
                        }
                    } else {
                        length1 = length1 / 2;
                        start1 = start1 + length1;
                    }
                }

            }
            median1 = medianNumber(nums1, start1, length1);
            median2 = medianNumber(nums2, start2, length2);
            if (median1 == median2) {
                length1 = length1 / 2;
                length2 = length2 / 2;
                start1 = start1 + length1 / 2;
                start2 = start2 + length2 / 2;
            } else {
                if (median1 > median2) {
                    length1 = length1 / 2;
                    length2 = length2 / 2;
                    start2 = start2 + length2;
                } else {
                    length1 = length1 / 2;
                    length2 = length2 / 2;
                    start1 = start1 + length1;
                }
            }
        }
        return 0;
    }

    private double getMedian(int[] nums, int start, int length, int num) { //一个树和数组，直接二分插入。
        //存在着代码的重复，故使用函数，使函数的思路更加清晰
        if (length % 2 == 0) { //有偶数个
            if (num < nums[start + length / 2 - 1]) {
                return nums[start + length / 2 - 1];
            }
            if (num > nums[start + length / 2]) {
                return nums[start + length / 2];
            } else {
                return num;
            }
        } else { //有奇数个元素
            if (num == nums[start + length / 2]) {
                return nums[start + length / 2];
            }
            if (num < nums[start + length / 2]) {
                if (num <= nums[start + length / 2 - 1]) {
                    return (nums[start + length / 2 - 1] + nums[start + length / 2]) / 2;
                } else {
                    return (num + nums[start + length / 2]) / 2;
                }
            } else {
                if (num <= nums[start + length / 2 + 1]) {
                    return (num + nums[start + length / 2]) / 2;
                } else {
                    return (nums[start + length / 2] + nums[start + length / 2 + 1]) / 2;
                }
            }

        }
    }

    private double medianNumber(int[] nums, int start, int length) {
        if (length % 2 == 0) {
            return (nums[start + length / 2 - 1] + nums[start + length / 2]) / 2.0;
        } else {
            return (double) nums[start + length / 2];
        }
    }
}
