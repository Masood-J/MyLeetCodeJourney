class Solution
{
public:
    int heightChecker(vector<int> &heights)
    {
        int incorrect_indices{0};
        vector<int> Expected_height;
        for (int i = 0; i < heights.size(); i++)
        {
            Expected_height.push_back(heights[i]);
        }

        for (int i = 0; i < Expected_height.size(); i++)
        {
            for (int j = i + 1; j < Expected_height.size(); j++)
            {
                if (Expected_height[i] > Expected_height[j])
                {
                    Expected_height[i] = Expected_height[i] + Expected_height[j];
                    Expected_height[j] = Expected_height[i] - Expected_height[j];
                    Expected_height[i] = Expected_height[i] - Expected_height[j];
                }
            }
        }

        for (int i = 0; i < Expected_height.size(); i++)
        {
            if (heights[i] != Expected_height[i])
            {
                incorrect_indices++;
            }
        }
        return incorrect_indices;
    }
};