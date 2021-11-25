#include <iostream>
#include <fstream>
#include <string>
#include "bitmap_def.h"
#include "tinybmp.h"
#include "tinybmp_low.h"
#include "tinybmp_high.h"
#include "tinybmp_resize.h"
#include "tinybmp_rotate.h"

int main(int argc, char* argv[])
{
	// low_pass_filter
  tiny_bitmap_low a("image.bmp");
	for(int i = 0 ; i < 15; i++)
		a.low_pass_filter();
	a.export_image("test1.bmp");

	



	 //high_pass_filter	
	tiny_bitmap_high b("image.bmp");
	for(int i=0 ; i< 30; i++)
		b.high_pass_filter();
	b.export_image("test2.bmp"); 




  // rotate
  tiny_bitmap_rotate c("image.bmp");
  c.rotate();
	c.export_image("test3.bmp");





	
	// resize_half
	  tiny_bitmap_resize d("image.bmp");
			d.resize_half();
	d.export_image("test4.bmp");






	// resize_expand
	tiny_bitmap_resize e("image(1).bmp");
			e.resize_expand();
	e.export_image("test5.bmp");




	return 0;
}