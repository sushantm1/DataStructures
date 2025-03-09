package sorting;

public class SelectionSort {
	static void selectSort(int arr[]) {
		int temp;
		for(int i=0;i<arr.length-1;i++) {
			for(int j=i+1;j<arr.length;j++) {
				if(arr[i]>arr[j]) {
					temp=arr[j];
					arr[j]=arr[i];
					arr[i]=temp;
				}
			}
		}
	}
	
	public static void main(String[] args) {
	int arr[]= {16,744,985,94,516,5296};
	System.out.println("prgm for Selection Sort");
	System.out.println("initial arr[]={16,744,985,94,516,5296,94}");
	selectSort(arr);
	System.out.print("[");
	for(int i:arr){System.out.print(i+", ");}
	System.out.print("]");

	}
}
