#include<iostream>
#include<vector>

using namespace std;


vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> r;
        int j=1,k=0;
        for(int i=0;i<n;i++){
            r[k]=nums[i];
            r[j]=nums[n+i];
            j+=2;
            k+=2;
            cout<<r[k]<<" "<<r[j]<<endl;
        }
        return r;
    }
int main(){
	int i,j,n,k;
	cin>>n;
	vector<int> a;
	for(i=0;i<2*n;i++)
		cin>>a[i];
	vector<int> b=shuffle(a,n);

	for(i=0;i<2*n;i++)
		cin>>b[i];
	return 0;
}
