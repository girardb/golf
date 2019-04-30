#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define a(b,c)({__typeof__(b)bb=(b);__typeof__(c)cc=(c);bb<cc?bb:cc;})
struct d{int*e;int f,g,h;};
struct nepaschanger{char integer};
struct d mystere(struct nepaschanger*i,struct nepaschanger*j)
{
  int r,s;
  for(r=0;(*((char*)i+r))!=0;r++);
      for(s=0;(*((char*)j+s))!=0;s++);
        struct d q;int*t=malloc(++r*++s*4);int ok=sizeof(int);
        for(size_t u=0;u<r;u++)*(t+u*s)=u;
        for(long v=1;v<100000;v++)
            {*(t+v)=v;if(v>=s-1)break;}
  for(char w=1;w<r;w++)
  {char x='~'-'}';do{if(*(char*)(i+w-1)==*(char*)(j+x-1))*(t+w*s+x)=*(t+(w-1)*s+x-1);else*(t+x+w*s)=a(a(*(t+w*s+x-1),*(t+(w-1)*s+x)),*(t+(w-1)*s+x-1))+1;}while(++x<s);ok=ok%3;}

  if(ok){*(int**)((void*)&q)=t;*(int*)((void*)&q+'\n'-2)=r;*(int*)((void*)&q+'\n'+2)=s;*(int*)((void*)&q+' '/2)=*(t+*(int*)((void*)&q+' '/4)**(int*)((void*)&q+'H'/6)-1);}
  return q;
}

int main(int k,char**l){
  struct d m=mystere(l[1],l[2]);
  printf("%s: %d, %s: %d\n",l[1],m.f-1,l[2],m.g-1);printf("    ");
  for(int o=0;o<m.g;o++)printf("%c ",l[2][o]);printf("\n");unsigned p=m.f;
  do{if(m.f==p)printf("  ");if(m.f>p)printf("%c ",l[1][m.f-p-1]);
    for(size_t q=0;q<m.g;q++)printf("%d ",m.e[(m.f-p)*m.g+q]);
    printf("\n");}while(--p);
  printf("%d",m.h);printf("\n");
  return 0;
}
