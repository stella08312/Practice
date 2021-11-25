#pragma once
#include "tinybmp.h"

class tiny_bitmap_rotate : public tiny_bitmap
{
public:
	tiny_bitmap_rotate(std::string file_name)
		:tiny_bitmap(file_name)
	{

	}
public:
	void rotate()
	{
    int XtoY;
		unsigned char** new_image_buf = create_bitmap_24bit(m_bih.width, m_bih.height);
		for(int i = 0; i < m_bih.width  ; i++)
		{
			for(int j = 0; j < m_bih.height*3 ; j+=3)
			{
				new_image_buf[m_bih.width -i-1][j] = m_image_buf[j/3][i*3-3];
				new_image_buf[m_bih.width -i-1][j+1] = m_image_buf[j/3][i*3-2];
				new_image_buf[m_bih.width -i-1][j+2] = m_image_buf[j/3][i*3-1];
			}
		}
    

		for(int i=0; i<m_bih.height;i++)
		{
			delete [] m_image_buf[i];
		}
		delete [] m_image_buf;

    std::cout << " " << std::endl;

    XtoY = m_bih.height;
    m_bih.height = m_bih.width;
    m_bih.width = XtoY;
    
		m_image_buf = new_image_buf;
	}
};