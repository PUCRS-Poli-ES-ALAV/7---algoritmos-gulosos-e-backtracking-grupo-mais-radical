public class nrainhas{
    public static void main(String args[]){
        int tabuleiro[][] = nrainhas(15);
        imprimeTabu(tabuleiro);
        boolean t = confirma(tabuleiro);
        System.out.println(t);
    }

    public static int[][] nrainhas(int n){
        int tabuleiro[][] = new int[n][n];
        int cont = 0;
        for(int i = 0; i<n ; i++){
            tabuleiro[cont][i] = 1;
            cont = cont + 2;
            if(cont >= n){
                cont = cont - n;
            }
        }
        return tabuleiro;
    }

    public static void imprimeTabu(int tabuleiro[][]){
        for(int i = 0; i < tabuleiro.length ; i++){
            for(int j = 0 ; j < tabuleiro[0].length; j++){
                System.out.print(tabuleiro[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static boolean confirma(int tabuleiro[][]){
        boolean eValido = true;
        for(int j = 0; j < tabuleiro[0].length; j++){
            for(int i = 0; i < tabuleiro.length; i++){
                //Encontra a rainha da coluna
                if(tabuleiro[i][j] == 1){
                    //verifica a linha que a rainha está
                    for(int l = 0; l < tabuleiro.length; l++){
                        if(tabuleiro[l][j] == 1 && l != i){
                            return false;
                        }
                        if(l != i){
                            tabuleiro[l][j] = 2;
                        }
                    }
                    //verifica a coluna que a rainha está
                    for(int c = 0; c < tabuleiro[0].length; c++){
                        if(tabuleiro[i][c] == 1 && c != j){
                            return false;
                        }
                        if(c != j){
                            tabuleiro[i][c] = 2;
                        }
                    }
                    /*int linha;
                    int coluna;

                    linha = i + 1;
                    coluna = j + 1;
                    while(linha < tabuleiro.length || coluna < tabuleiro[0].length){
                        if(tabuleiro[linha][coluna] == 1 && linha != i && coluna != j){
                            return false;
                        }
                        tabuleiro[linha][coluna] = 2;
                        linha++;
                        coluna++;
                    }*/

                }
            }
        }
        System.out.println();
        imprimeTabu(tabuleiro);
        return true;
    }
}