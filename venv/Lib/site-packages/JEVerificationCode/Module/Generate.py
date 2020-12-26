import base64
import os
import random
from io import BytesIO

import matplotlib.font_manager as fm
from PIL import Image, ImageDraw, ImageFont


class GenerateVerificationCode:

    @staticmethod
    def generate_color(color_r=255, color_g=255, color_b=255):
        """
        :param color_r: Color R
        :param color_g: Color G
        :param color_b: Color B
        :return: R,G,B
        """
        return random.randint(0, color_r), random.randint(0, color_g), random.randint(0, color_b)

    def generate_picture(self, picture_width=175, picture_height=55):
        """
        :param picture_width: Image Width
        :param picture_height: Image Height
        :return: Picture with color
        """
        return Image.new('RGB', (picture_width, picture_height), self.generate_color())

    @staticmethod
    def generate_string():
        num = str(random.randint(0, 9))
        low_alpha = chr(random.randint(97, 122))
        return random.choice([num, low_alpha])

    def generate_code_only_string(self, count):
        temp = []
        for i in range(count):
            chars = self.generate_string()
            temp.append(chars)
        valid = "".join(temp)
        return valid

    def generate_code(self, count, image, font_size):
        """
        :param count: Code Count
        :param image: draw Code Image
        :param font_size: font's size
        :return: Code picture
        """
        draw = ImageDraw.Draw(image)
        font_file = os.path.join('arial.ttf')
        try:
            font = ImageFont.truetype(font_file, size=font_size)
        except OSError:
            font = ImageFont.truetype(fm.findfont(fm.FontProperties(family='DejaVu Sans')), font_size)
        temp = []
        for i in range(count):
            chars = self.generate_string()
            draw.text((10 + i * 30, -2), chars, self.generate_color(), font)
            temp.append(chars)
        valid = "".join(temp)
        return valid, image

    def generate_noise(self, image, picture_width=175, picture_height=55, line_count=3, point_count=15):
        """
        :param image: Noise Image
        :param picture_width: Image Width
        :param picture_height: Image Hieght
        :param line_count: Line's count
        :param point_count: Point's count
        :return: After Noise Image
        """

        draw = ImageDraw.Draw(image)

        # draw Line
        for i in range(line_count):
            x1 = random.randint(0, picture_width)
            x2 = random.randint(0, picture_width)
            y1 = random.randint(0, picture_height)
            y2 = random.randint(0, picture_height)
            draw.line((x1, y1, x2, y2), fill=self.generate_color())

            # draw Point
            for point in range(point_count):
                draw.point([random.randint(0, picture_width), random.randint(0, picture_height)],
                           fill=self.generate_color())
                x = random.randint(0, picture_width)
                y = random.randint(0, picture_height)
                draw.arc((x, y, x + 4, y + 4), 0, 90, fill=self.generate_color())

        return image

    def generate_base64_image(self, code_count, font_size, save=False):

        code_image = self.generate_picture()
        valid, code_image = self.generate_code(code_count, code_image, font_size)
        code_image = self.generate_noise(code_image)

        if save:
            code_image.save('code_image.jpeg')

        byte = BytesIO()
        code_image.save(byte, 'jpeg')
        data = byte.getvalue()
        byte.close()

        encode64 = base64.b64encode(data)
        data = str(encode64, encoding='utf-8')
        image_data = "data:image/jpeg;base64,{data}".format(data=data)
        return valid, image_data
