"""ЛР7 вариант 4. Булова Екатерина, БИ 2-1."""
import time,statistics,matplotlib.pyplot as plt
calls=0
def naive(n):
 global calls
 calls+=1
 if n<0:return 0
 if n==0:return 1
 return naive(n-1)+naive(n-2)+naive(n-3)
def memo(n,m=None):
 global calls
 calls+=1
 if m is None:m={}
 if n<0:return 0
 if n==0:return 1
 if n not in m:m[n]=memo(n-1,m)+memo(n-2,m)+memo(n-3,m)
 return m[n]
def iterative(n):
 d=[0]*(n+1);d[0]=1
 for i in range(1,n+1):d[i]=sum(d[i-j] for j in (1,2,3) if i>=j)
 return d[n]
def coin_dp(S,coins):
 d=[S+1]*(S+1);p=[-1]*(S+1);d[0]=0
 for s in range(1,S+1):
  for c in coins:
   if c<=s and d[s-c]+1<d[s]:d[s]=d[s-c]+1;p[s]=c
 out=[];s=S
 while s:c=p[s];out.append(c);s-=c
 return d[S],out
def main():
 global calls
 for n in (10,15,20,24,28):
  calls=0;t=time.perf_counter();a=naive(n);tn=time.perf_counter()-t;cn=calls
  calls=0;t=time.perf_counter();b=memo(n);tm=time.perf_counter()-t;cm=calls
  t=time.perf_counter();c=iterative(n);ti=time.perf_counter()-t
  assert a==b==c
  print(n,a,cn,cm,tn,tm,ti)
 cnt,used=coin_dp(200,[1,3,7]);print('Размен',cnt,{c:used.count(c) for c in [1,3,7]})
 sums=[100,200,400,800,1200,1600,2000,3000,4000];times=[]
 for S in sums:
  ts=[]
  for _ in range(5):
   t=time.perf_counter();coin_dp(S,[1,3,7]);ts.append(time.perf_counter()-t)
  times.append(statistics.median(ts))
  print('Г4',S,times[-1])
 plt.plot(sums,times,marker='o');plt.grid();plt.xlabel('S');plt.ylabel('Время ДП');plt.savefig('g4_time.png')
if __name__=='__main__':main()
