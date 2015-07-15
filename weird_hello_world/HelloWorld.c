#include <stdio.h>


int main(){
//since by default padding is 16 bytes with gcc, just compile with no special flags
//this only works if ints are 4 bytes
	int i[] = {328,839,301,2320,261996};
	int a[1];
	int (*test)[4] = &i;
	test[2][0] = (int)(char)test[0][0]; //so it casts as a char, then an int. casting char->int pads upper parts with 0s. int->char takes first byte which for little endian is the lower values of the int
	printf("%c", (char)a[0]);
	i[(int)(char)i[0] - (int)(char)i[1] ]= i[0] ^ (int)(((char*)"Hello")[4] + 190);
	test[2][0] = (int)(char)test[0][1];
	printf("%c", a[0]);
	a[0] = *test[1];
	printf("%c",a[0]);
	printf("%c",i[4]);
	printf("%c", (char)(i[2] - 190));
	printf("%c", (char)(test[0][3] <<1));
	printf("%c", ((((char)i[4]) >>2  ) | (char)(test[0][3] <<1)) + ((((unsigned int)&a %1000) - ((unsigned int)&test[0])%1000)) - 4);//technically this line can fail, depending on the memory addresses  of the arrays. if it's something like xxxx1002 and xxxxx970, it's going to fuck up	
	printf("%c", (char)(i[2] - 190));
	printf("r");
	printf("%c",i[4]);
	printf("d");
	printf("\n");
	return 0;
}

