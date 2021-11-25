#pragma once

class tiny_bitmap
{
public:
	tiny_bitmap(std::string file_name)
		:m_image_buf(NULL)
	{
	   std::ifstream fin;
	   fin.open(file_name.c_str(), std::ios::binary);

	   fin.read((char*)&m_bh, sizeof(BITMAP_HEADER));
	   fin.read((char*)&m_bih, sizeof(BITMAP_INFO_HEADER));

	   if(m_bh.type !=0x4D42)
	   {

		   fin.close();
		   std::cerr << "[ERROR] tiny.bitmap::tiny_bitmap() Invalid Image File" <<std::endl;
		   exit(1);
	   }

	   m_image_buf = create_bitmap_24bit(m_bih.height, m_bih.width);
	   char padding_buf[4];
	   for(int i=0 ; i<m_bih.height ; i++)
	   {
		   fin.read((char*)(m_image_buf[m_bih.height-1-i]),m_bih.width * 3);
		   if((m_bih.width % 4) != 0)
		   {
			   fin.read(padding_buf, (m_bih.width % 4));
		   }
	   }

	   fin.close();
	}

	void export_image(std::string file_name)
	{
		std::ofstream fout;

		fout.open(file_name.c_str(), std::ios::binary);

		fout.write((char*)&m_bh, sizeof(BITMAP_HEADER));
		fout.write((char*)&m_bih, sizeof(BITMAP_INFO_HEADER));

		char padding_buf[4] = {0,0,0,0};
		for(int i=0 ; i<m_bih.height ; i++)
		{
			for(int j=0 ; j<m_bih.width *3 ; j+=3)
			{
				fout.write((char*)(m_image_buf[m_bih.height-1-i]+j), sizeof(unsigned char));
				fout.write((char*)(m_image_buf[m_bih.height-1-i]+j+1), sizeof(unsigned char));
				fout.write((char*)(m_image_buf[m_bih.height-1-i]+j+2), sizeof(unsigned char));
			}

			if((m_bih.width % 4) !=0)
			{
				fout.write(padding_buf, (m_bih.width % 4));
			}
		}
	}

protected:
	unsigned char** create_bitmap_24bit(int height, int width)
	{
		unsigned char** image_buf;
		image_buf = new unsigned char*[height];
		for(int i=0 ; i < height ; i++)
		{
			image_buf[i] = new unsigned char[width*3];
		}

		return image_buf;
	}

	~tiny_bitmap()
	{
		if(m_image_buf != NULL)
		{
			delete [] m_image_buf;
			m_image_buf = NULL ;
		}
	}

protected:
	BITMAP_HEADER m_bh;
	BITMAP_INFO_HEADER m_bih;
	unsigned char** m_image_buf;

};