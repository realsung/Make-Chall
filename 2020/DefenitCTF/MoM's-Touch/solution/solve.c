#include <stdio.h>
#include <stdlib.h>

unsigned int table[74] = {186,28,4,248,59,168,156,124,142,152,129,137,9,85,208,238,197,253,71,80,162,70,223,99,46,81,56,254,106,242,160,90,148,229,73,98,55,31,121,216,84,28,229,104,187,240,96,100,15,73,205,125,169,253,2,125,202,3,50,128,197,75,61,233,116,141,61,138,44,178,48,120,196};
unsigned int tmp;
unsigned int table2[0x101];

void create(){
	srand(0xff);
	tmp = rand() % 0xff;
	for(int i=0; i<=0xff; i++){
		table2[i] = rand() % 0xff;
	}
}

int main(){
	create();
	unsigned int go;
	unsigned int tmp2;
	unsigned int tmp3;
	for(int i=0; i<73; i++){
		int tmp1 = rand() % 0xff;
		tmp2 = (table2[i] << 4) | (table2[i] >> 4);
		tmp2 = tmp2 & 0xff;
		tmp3 = tmp1;
		tmp3 = (tmp3 << 2) | (tmp3 >> 2);
		tmp3 = tmp3 & 0xff;
		go = table[i] ^ table2[tmp2] ^ table2[tmp3];
		printf("%c",go);
	
	}
}