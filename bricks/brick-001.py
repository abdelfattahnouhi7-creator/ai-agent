def average(nums):
    if not isinstance(nums, (list, tuple)) or not nums:
        raise ValueError("Invalid input - الليستة خاوية ولا ماشي ليستة")
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("Invalid input - فيها شي حاجة ماشي رقم")
    return sum(nums) / len(nums)
