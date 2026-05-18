class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {

        if (m == 0)
        {
            for (int i = 0; i < nums1.size(); i++)
            {
                nums1[i] = nums2[i];
            }
            return;
        }
        for (int i = nums1.size() - 1, j = 0; i >= nums1.size() - nums2.size(); i--, j++)
        {
            nums1[i] = nums2[j];
        }
        for (int i = 0; i < nums1.size(); i++)
        {
            for (int j = i + 1; j < nums1.size(); j++)
            {
                if (nums1[i] > nums1[j])
                {
                    nums1[i] = nums1[i] + nums1[j];
                    nums1[j] = nums1[i] - nums1[j];
                    nums1[i] = nums1[i] - nums1[j];
                }
            }
        }
    }
};