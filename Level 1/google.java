
class Test
{
  static final int MAX_SIZE = 1000001;

  static Vector<Boolean>isPrime = new Vector<>(MAX_SIZE);
  static Vector<Integer>prime = new Vector<>();
  static Vector<Integer>SPF = new Vector<>(MAX_SIZE);

  static void mani_sieve(int N){

    isPrime.set(0,false);
    isPrime.set(1,false);

    for(int i=2;i<N;i++){
      if(isPrime.get(i)){
        prime.add(i);
        SPF.set(i,i);
      }

      for(int j=0;j<prime.size() && i*prime.get(j)<N && prime.get(j) <= SPF.get(i);j++){
        isPrime.set(i*prime.get(j),false);

        SPF.set(i*prime.get(j),prime.get(j));
      }
    }
  }

  public static String answer(int n){

  }

  public static void main(String args[]){
    int N= 50000;

    for (int i=0;i<MAX_SIZE;i++){
      isPrime.add(true);
      SPF.add(2);
    }

    mani_sieve(N);

    for(int i=0;i<prime.size()&& prime.get(i)<=N;i++){
      System.out.print(prime.get(i)+"");
    }
  }
}
