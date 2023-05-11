int binarySearch(vector<int> v, int x) {
    int left = 0;
    int right = v.size()-1;

    while (left <= right) {
        int mid = (left + right)/2;

        if (v[mid] == x) {
            return mid;
        }
        else if (v[mid] < x) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return -1;
}
