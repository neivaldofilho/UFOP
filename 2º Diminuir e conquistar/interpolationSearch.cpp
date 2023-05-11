int interpolationSearch(int A[], int n, int target)
{
   if (n == 0) {
        return -1;
    }
    int low = 0, high = n - 1, mid;

    while (A[high] != A[low] && target >= A[low] && target <= A[high])
    {
        mid = low + ((target - A[low]) * (high - low) / (A[high] - A[low]));

        if (target == A[mid]) {
            return mid;
        }
        else if (target < A[mid]) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    if (target == A[low]) {
        return low;
    }

    else {
        return -1;
    }
}
