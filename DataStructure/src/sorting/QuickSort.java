package sorting;

public class QuickSort {
	int partition(int arr[],int low,int high) {
		int pivot=high-1;
		int i=low-1;
		int temp=0;
		for(int j=low;j<=high;j++) {
			if(arr[j]<=pivot) {
				i++;
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
		temp=arr[i+1];
		arr[i+1]=arr[high];
		arr[high]=temp;
		return i+1;
	}
	
	void quicksort(int arr[],int low=0,int high=null) {
		
	}
	
	public static void main(String[] args) {
		int arr[]= {23,3,45,2,34,45,2,3};
		
	}
}
