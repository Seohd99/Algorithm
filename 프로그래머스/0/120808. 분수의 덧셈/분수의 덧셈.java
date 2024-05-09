class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {};
        
        int son = numer1 *denom2 + numer2 * denom1;
        int mother = denom1 * denom2 ;
        int t = gcd(son, mother);
        son = son/t;
        mother = mother/t;
        
        answer = new int[]{son,mother} ;
        return answer;
    }
    public static int gcd(int son , int amy){
        int r =0;
        while(amy !=0){
            r = son%amy;
            son = amy;
            amy = r;
        }
        return son;
    }
}