#pragma once
#include "tinybmp.h"

class tiny_bitmap_resize : public tiny_bitmap
{
public:
	tiny_bitmap_resize(std::string file_name)
		:tiny_bitmap(file_name)
	{

	}
public:
	void resize_half()
	{
  
		unsigned char** new_image_buf = create_bitmap_24bit(m_bih.height, m_bih.width);
    
    
		for(int i = 1; i<(m_bih.height-1)/2; i++)
		{
			for(int j = 3; j < (m_bih.width-1)*3/2 ; j+=3)
			{
        new_image_buf[i][j] = m_image_buf[(i-1)*2][j*2];		
				new_image_buf[i][j+1] = m_image_buf[(i-1)*2][(j*2+1)];
				new_image_buf[i][j+2] = m_image_buf[(i-1)*2][(j*2+2)];
        
			}
		}

		for(int i=0; i<m_bih.height;i++)
		{
			delete [] m_image_buf[i];
		}
		delete [] m_image_buf;
    
    m_image_buf = new_image_buf;

    m_bih.height = m_bih.height/2;
    m_bih.width = m_bih.width/2;
	 }


  void resize_expand()
	{

		unsigned char** new_image_buf = create_bitmap_24bit(m_bih.height*2, m_bih.width*2);
		
    for(int i = 1; i<(m_bih.height-1); i++)
		{
			for(int j = 3; j < (m_bih.width-1)*3 ; j+=3)
			{
         new_image_buf[i*2][j*2+3] = m_image_buf[i][j];
         new_image_buf[i*2][j*2] = m_image_buf[i][j];
         new_image_buf[i*2+1][j*2+3] = m_image_buf[i][j];
         new_image_buf[i*2+1][j*2] = m_image_buf[i][j];
         

         new_image_buf[i*2][j*2+1+3] = m_image_buf[i][j+1];
         new_image_buf[i*2][j*2+1] = m_image_buf[i][j+1];
         new_image_buf[i*2+1][j*2+1+3] = m_image_buf[i][j+1];
         new_image_buf[i*2+1][j*2+1] = m_image_buf[i][j+1];
         

         new_image_buf[i*2][j*2+2+3] = m_image_buf[i][j+2];
         new_image_buf[i*2][j*2+2] = m_image_buf[i][j+2];
         new_image_buf[i*2+1][j*2+2+3] = m_image_buf[i][j+2];
         new_image_buf[i*2+1][j*2+2] = m_image_buf[i][j+2];
			}
		}

		for(int i=0; i<m_bih.height;i++)
		{
			delete [] m_image_buf[i];
		}
		  delete [] m_image_buf;

		m_image_buf = new_image_buf;

    m_bih.height = m_bih.height*2;
    m_bih.width = m_bih.width*2;
   
	}
};