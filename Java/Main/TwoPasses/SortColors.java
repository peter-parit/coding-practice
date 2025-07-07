package TwoPasses;

class SortColors {
    public void sortColors(int[] nums) {
        int countReds = 0;
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            if (nums[left] == 0) {
                countReds++;
                left++;
                continue;
            } else {
                while (nums[right] != 0 && left != right) right--;
                if (nums[right] == 0 && left != right) {
                    countReds++;
                    nums[right] = nums[left];
                    nums[left] = 0;
                }
            }
            left++;
        }
        left = countReds;
        right = nums.length - 1;
        while (left < right) {
            if (nums[left] != 1) {
                while (nums[right] != 1 && left != right) right--;
                if (nums[right] == 1 && left != right) {
                    nums[right] = nums[left];
                    nums[left] = 1;
                }
            }
            left++;
        }
    }
}