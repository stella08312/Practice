#pragma once
#include "tinybmp.h"

class tiny_bitmap_low : public tiny_bitmap
{
public:
	tiny_bitmap_low(std::string file_name)
		:tiny_bitmap(file_name)
	{

	}
public:
	void low_pass_filter()
	{
		double filter[3][3] = {{1/9.0,1/9.0,1/9.0},{1/9.0,1/9.0,1/9.0},{1/9.0,1/9.0,1/9.0}};

		unsigned char** new_image_buf = create_bitmap_24bit(m_bih.height, m_bih.width);
		for(int i = 1; i<m_bih.height -1 ; i++)
		{
			for(int j = 3; j < (m_bih.width-1)*3 ; j+=3)
			{
				new_image_buf[i][j] = m_image_buf[i-1][j-3]*filter[0][0] +
					m_image_buf[i-1][j  ]*filter[0][1]+
					m_image_buf[i-1][j+3]*filter[0][2]+
					m_image_buf[i  ][j-3]*filter[1][0]+
					m_image_buf[i  ][j  ]*filter[1][1]+
					m_image_buf[i  ][j+3]*filter[1][2]+
					m_image_buf[i+1][j-3]*filter[2][0]+
					m_image_buf[i+1][j  ]*filter[2][1]+
					m_image_buf[i+1][j+3]*filter[2][2];
					
				new_image_buf[i][j+1] = m_image_buf[i-1][j-2]*filter[0][0] +
					m_image_buf[i-1][j+1  ]*filter[0][1]+
					m_image_buf[i-1][j+4]*filter[0][2]+
					m_image_buf[i  ][j-2]*filter[1][0]+
					m_image_buf[i  ][j+1]*filter[1][1]+
					m_image_buf[i  ][j+4]*filter[1][2]+
					m_image_buf[i+1][j-2]*filter[2][0]+
					m_image_buf[i+1][j+1]*filter[2][1]+
					m_image_buf[i+1][j+4]*filter[2][2];

				new_image_buf[i][j+2] = m_image_buf[i-1][j-1]*filter[0][0] +
					m_image_buf[i-1][j+2]*filter[0][1]+
					m_image_buf[i-1][j+5]*filter[0][2]+
					m_image_buf[i  ][j-1]*filter[1][0]+
					m_image_buf[i  ][j+2]*filter[1][1]+
					m_image_buf[i  ][j+5]*filter[1][2]+
					m_image_buf[i+1][j-1]*filter[2][0]+
					m_image_buf[i+1][j+2]*filter[2][1]+
					m_image_buf[i+1][j+5]*filter[2][2];
			}
		}

		for(int i=0; i<m_bih.height;i++)
		{
			delete [] m_image_buf[i];
		}
		delete [] m_image_buf;

		m_image_buf = new_image_buf;
	}
};