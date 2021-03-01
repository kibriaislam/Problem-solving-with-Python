#include<bits/stdc++.h>
#define mx 1000000
#define p 15002
using namespace std;
int prime[mx],c=1;
bool status[mx];
void siv()
{
	int sq=sqrt(mx);
	for(int i=4;i<=mx;i+=2) status[i]=1;
	for(int i=3;i<=sq;i+=2){
		if(status[i]==0)
		{
			for(int j=i*i;j<mx;j+=i) status[j]=1;
		}
	}
	status[1]=1;
	for(int i=1;i<mx;i++)
    {
        if(status[i]!=1)prime[c++]=i;
    }
cout<<c<<endl;
}

int main()
{
    int n,m;
    siv();
    cin>>n;
    while(n--)
    {
        cin>>m;
        cout<<prime[m]<<endl;;
    }
}
