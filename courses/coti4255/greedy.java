import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Greedy {

	public static void main(String[] args) {
		
		int [] arrWl = {100,200,140,600};
		int [] items = {50,60,70,100,50,41,25,78,90,41,600};
		int [] arrWlcopy = Arrays.copyOf(arrWl, arrWl.length);
		int [] arrIdx = sortIdx(arrWl);
		descendingSort(arrWl);
		items = descendingSort(items);
		
		ArrayList< ArrayList<Integer> > Loading = new ArrayList< ArrayList<Integer> >(arrWl.length);
	
		for(int x = 0; x < arrWl.length; x++) {
			int acum = 0;
			ArrayList<Integer> Cargo = new ArrayList<Integer>();
			for(int y = 0; y < items.length; y++) {
				if(arrWl[x] >= acum + items[y] && arrWl[x] > 0) {
					acum += items[y];
					if(items[y] > 0)
						Cargo.add(items[y]);
					items[y] = -1;
				}
			}
			Loading.add(Cargo);
		}
		printReport(arrWlcopy,arrIdx,Loading);
	}

	/*
	 * Metodo para imprimir reporte
	 * */
	private static void printReport(int[] arrWlcopy, int[] arrIdx, ArrayList<ArrayList<Integer>> loading) {
		
		/*
		 * Se invierte el arreglo al orden original.
		 * */
		for(int i = 0 ; i < arrIdx.length;i++)
	    {
	        for(int j = i+1 ; j< arrIdx.length;j++)
	        {
	            if(arrIdx[i] > arrIdx[j])
	            {
	                ArrayList<Integer> temp = loading.get(i);
	                loading.set(i, loading.get(j));
	                loading.set(j,temp);
	                
	            	int temp2 = arrIdx[i];
	            	arrIdx[i] = arrIdx[j];
	            	arrIdx[j] = temp2;
	            	
	            }
	        }
	    }
		/*
		 * Se prepara el modelo del reporte.
		 * */
		for(int y = 0; y < arrWlcopy.length; y++) {
			System.out.print(arrWlcopy[y] + " -> (");
			Object [] tempArr = loading.get(y).toArray();
			int acum = 0;
			for(int z = 0; z < tempArr.length ;z++) {
				acum += (Integer)tempArr[z];
				if(z == tempArr.length -1)
					System.out.printf("%d", tempArr[z]);
				else
					System.out.printf("%d, ", tempArr[z]);
			}
			System.out.println(") = " + acum );
		}
		
	}

	/*
	 * Metodo para extraer el orden original a nivel indices 
	 * de un arreglo que fue sorteado descendentemente.
	 * */
	private static int[] sortIdx(int[] arr) {
		int temp = 0, temp2 = 0;
		int [] arrIdx = new int [arr.length];
		
		//Llena el arreglo indice
		for(int x = 0; x < arr.length ; x++)
			arrIdx[x] = x;
		
		for (int i = 0; i < arr.length; i++) {     
            for (int j = i+1; j < arr.length; j++) {     
               if(arr[i] < arr[j]) { 
            	   
            	   temp2 = arr[i];    
                   arr[i] = arr[j];    
                   arr[j] = temp2;
            	   
            	   temp = arrIdx[i];    
                   arrIdx[i] = arrIdx[j];    
                   arrIdx[j] = temp;   
               }     
            }     
        }
		return arrIdx;
	}

	/*
	 * Metodo para ordenar un arreglo de manera decendente
	 * */
	private static int[] descendingSort(int[] arrWl) {
		int temp = 0;
		for (int i = 0; i < arrWl.length; i++) {     
            for (int j = i+1; j < arrWl.length; j++) {     
               if(arrWl[i] < arrWl[j]) {    
                   temp = arrWl[i];    
                   arrWl[i] = arrWl[j];    
                   arrWl[j] = temp;    
               }     
            }     
        }    
		return arrWl;
	}

}

