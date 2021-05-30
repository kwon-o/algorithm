import java.util.Scanner;

public class baek_2517_달리기 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		
		int[] race = new int[num];
		int[] temp = new int[num];
	
		for(int i=0; i<race.length; i++) {
			race[i] = scan.nextInt();
			temp[i] = 1;
		}
		
		for(int i=race.length-1; i>0; i--) {
			for(int j=i-1; j>=0; j--) {
				if(race[j]>race[i]) {
					temp[i]+=1;
				}
			}
		}
		
		for(int i=0; i<temp.length; i++) {
			System.out.println(temp[i]);
		}
	}
}
