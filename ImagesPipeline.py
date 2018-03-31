import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

# class DouyuagainPipeline(object):
#     def process_item(self, item, spider):
#         return item
class DouyuagainPipeline(ImagesPipeline):
    Image_STORE = get_project_settings().get('IMAGES_STORE')  # 默认路径
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        url = item['img_url']
        yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        print('---------------------------')
        # 下载到临时文件 reslut [( 下载成功,path),]
        image_path = [x['path'] for ok, x in results if ok]
        # 重命名
        try:
            os.rename(self.Image_STORE + '\\' + image_path[0], self.Image_STORE + '\\' + item['name'] + '.jpg')
        except:
            print('error')
        return item